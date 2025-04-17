import os
import sys
import time
import csv
import psutil
import threading

# Add the io_calculations folder to the Python path
io_calculations_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../io_calculations'))
sys.path.append(io_calculations_path)

from io_low import io_low  # Function for low I/O usage experiment
from io_medium import io_medium  # Function for medium I/O usage experiment
from io_long import io_long  # Function for long I/O usage experiment


def log_results(duration, experiment_name, run_number, start_time, finish_time):
    """
    Logs the duration of an experiment to a CSV file.

    Args:
        duration (float): Duration of the experiment in seconds.
        experiment_name (str): Name of the experiment.
        run_number (int): Run number of the experiment.
    """
    log_path = os.path.join(LOG_DIR, f"{experiment_name}_inside_time.csv")

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


def run_experiment(func, name, run_number, io_path):
    """
    Runs an experiment and logs its I/O usage and duration.

    Args:
        func (function): The experiment function to run.
        name (str): Name of the experiment.
        run_number (int): Run number of the experiment.
    """
    stop_event = threading.Event()  # Event to signal when to stop I/O logging
    io_logger = threading.Thread(target=log_io_usage, args=(name, run_number, stop_event))  # I/O logging thread
    io_logger.start()  # Start the I/O logging thread

    start_time = time.time()  # Record the start time

    func(io_path)  # Run the experiment function

    finish_time = time.time()  # Record the finish time
    duration = finish_time - start_time  # Calculate the duration

    stop_event.set()  # Signal the I/O logging thread to stop
    io_logger.join()  # Wait for the I/O logging thread to finish

    log_results(duration, name, run_number, start_time, finish_time)  # Log the experiment duration


if __name__ == "__main__":
    """
    Main entry point for the script. Parses command-line arguments and runs the specified experiment.
    """

    if len(sys.argv) != 4:
        print("Usage: python3 io_test.py <experiment_name> <run_number> <test_type>")
        sys.exit(1)

    experiment_name = sys.argv[1]  # Name of the experiment
    run_number = int(sys.argv[2])  # Run number of the experiment
    test_type = sys.argv[3]

    io_path = "/mnt/usb/test_io.txt"
    # io_path = "/app/usb/test_io.txt"  # Path to the I/O t  est file

    # Ensure the logs directory exists
    # Logs will be stored in the "logs/io_logs" directory relative to the project root
    LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../logs/io_logs", test_type))              #"../../../logs/io_logs", /app/logs
    os.makedirs(LOG_DIR, exist_ok=True)

    # Map experiment names to their corresponding functions
    function_map = {
        "io_low": io_low,
        "io_medium": io_medium,
        "io_long": io_long
    }

    # Run the specified experiment
    run_experiment(function_map[experiment_name], experiment_name, run_number, io_path)