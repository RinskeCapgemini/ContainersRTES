import os
import sys
import time
import csv
import psutil
import threading

def log_results(duration, experiment_name, run_number, start_time, finish_time):
    """
    Logs the duration of an experiment to a CSV file.

    Args:
        duration (float): Duration of the experiment in seconds.
        experiment_name (str): Name of the experiment.
        run_number (int): Run number of the experiment.
    """
    log_path = os.path.join(LOG_DIR, f"{experiment_name}_program_time.csv")

    with open(log_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write the header if the file is empty
        if os.stat(log_path).st_size == 0:
            writer.writerow(["Experiment Name", "Run Number", "Start Time", "Finish Time", "Duration (s)"])

        # Log the experiment details
        writer.writerow([experiment_name, run_number, start_time, finish_time, duration])


def log_io_usage(experiment_name, run_number, stop_event):
    """
    Logs I/O speed (bytes per second) of the current process to a CSV file at regular intervals.

    Args:
        experiment_name (str): Name of the experiment.
        run_number (int): Run number of the experiment.
        stop_event (threading.Event): Event to signal when logging should stop.
    """
    process = psutil.Process(os.getpid())  # Get the current process
    io_log_path = os.path.join(LOG_DIR, f"{experiment_name}_speed.csv")

    with open(io_log_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write the header if the file is empty
        if os.stat(io_log_path).st_size == 0:
            writer.writerow(["Experiment Name", "Run Number", "Timestamp (s)", "Read Speed (B/s)", "Write Speed (B/s)"])

        start_time = time.time()
        prev_time = start_time
        prev_io_counters = process.io_counters()  # Get initial I/O counters

        # Log I/O speed until the stop event is set
        while not stop_event.is_set():
            current_time = time.time()
            io_counters = process.io_counters()  # Get current I/O counters

            # Calculate elapsed time and I/O speed
            elapsed_time = current_time - prev_time
            read_speed = (io_counters.read_bytes - prev_io_counters.read_bytes) / elapsed_time
            write_speed = (io_counters.write_bytes - prev_io_counters.write_bytes) / elapsed_time

            # Log the I/O speed
            timestamp = current_time - start_time
            writer.writerow([experiment_name, run_number, f"{timestamp:.2f}", f"{read_speed:.2f}", f"{write_speed:.2f}"])

            # Update previous values
            prev_time = current_time
            prev_io_counters = io_counters

            time.sleep(0.1)  # Log every 0.1 seconds


def read_1gb_binary(io_path):
    """
    Reads a 1 GB binary file from the specified path to ensure it is actually being read.

    Args:
        io_path (str): Path to the binary file on the USB device.
    """
    try:
        total_bytes_read = 0
        with open(io_path, 'rb') as f:
            while True:
                # Read in chunks of 1 MB
                data = f.read(1 * 1024 * 1024)  # 1 MB
                
                if not data:
                    break  # End of file
                
                total_bytes_read += len(data)
        
        print(f"Total bytes read: {total_bytes_read}")

    except Exception as e:
        print(f"Error while reading the file: {e}")
        sys.exit(1)


def run_experiment(name, run_number, io_path):
    """
    Runs an experiment and logs its I/O usage and duration.

    Args:
        name (str): Name of the experiment.
        run_number (int): Run number of the experiment.
        io_path (str): Path to the binary file to read.
    """
    stop_event = threading.Event()  # Event to signal when to stop I/O logging
    io_logger = threading.Thread(target=log_io_usage, args=(name, run_number, stop_event))  # I/O logging thread
    io_logger.start()  # Start the I/O logging thread

    start_time = time.time()  # Record the start time

    # Call the function to read the binary file
    read_1gb_binary(io_path)

    finish_time = time.time()  # Record the finish time
    duration = finish_time - start_time  # Calculate the duration

    stop_event.set()  # Signal the I/O logging thread to stop
    io_logger.join()  # Wait for the I/O logging thread to finish

    log_results(duration, name, run_number, start_time, finish_time)  # Log the experiment duration


if __name__ == "__main__":
    io_path = "/mnt/usb/1GB.bin"            # TODO: Change to filename
    # io_path = "/app/usb/test_io.txt"  # Path to the I/O test file


    run_number = int(sys.argv[1])   # Run number of the experiment
    test_type = sys.argv[2]         # control or experiment 


    # Ensure the logs directory exists
    # Logs will be stored in the "logs/io_logs" directory relative to the project root
    LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../logs/io_logs/i2", test_type))              #"../../../logs/io_logs/i2", /app/logs
    os.makedirs(LOG_DIR, exist_ok=True)

    run_experiment(test_type, run_number, io_path)