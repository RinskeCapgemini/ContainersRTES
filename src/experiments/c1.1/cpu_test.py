import time
import os
import psutil
import sys
import csv
import threading

# Add the memory_calculations folder to the Python path
# This allows importing memory calculation functions from the specified directory
memory_calculations_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../cpu_calculations'))
sys.path.append(memory_calculations_path)

from cpu_low import cpu_low  # Function for low cpu usage experiment
from cpu_medium import cpu_medium  # Function for medium cpu usage experiment
from cpu_long import cpu_long  # Function for long cpu usage experiment

def log_results(duration, experiment_name, run_number, start_time, finish_time):
    """
    Logs the duration of an experiment to a CSV file.

    Args:
        duration (float): Duration of the experiment in seconds.
        experiment_name (str): Name of the experiment.
        run_number (int): Run number of the experiment.
    """
    log_path = os.path.join(LOG_DIR, f"{experiment_name}_time.csv")

    with open(log_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write the header if the file is empty
        if os.stat(log_path).st_size == 0:
            writer.writerow(["Experiment Name", "Run Number", "Start Time", "Finish Time", "Duration (s)"])

        # Log the experiment details
        writer.writerow([experiment_name, run_number, start_time, finish_time, duration])
        
# def log_memory_usage(experiment_name, run_number, stop_event):
#     """
#     Logs memory usage of the current process to a CSV file at regular intervals.

#     Args:
#         experiment_name (str): Name of the experiment.
#         stop_event (threading.Event): Event to signal when logging should stop.
#     """
#     process = psutil.Process(os.getpid())  # Get the current process
#     memory_log_path = os.path.join(LOG_DIR, f"{experiment_name}_usage.csv")

#     with open(memory_log_path, 'a', newline='') as csv_file:
#         writer = csv.writer(csv_file)

#         # Write the header if the file is empty
#         if os.stat(memory_log_path).st_size == 0:
#             writer.writerow(["Experiment Name", "Run Number", "Timestamp (s)", "Memory Usage (MB)"])

#         start_time = time.time()

#         # Log memory usage until the stop event is set
#         while not stop_event.is_set():
#             mem_usage_mb = process.memory_info().rss / 1024 / 1024  # Convert memory usage to MB
#             timestamp = time.time() - start_time  # Calculate elapsed time
#             writer.writerow([experiment_name, run_number, f"{timestamp:.2f}", f"{mem_usage_mb:.2f}"])
#             time.sleep(0.1)  # Log every 0.1 seconds

def run_experiment(func, name, run_number):
    """
    Runs an experiment and logs its memory usage and duration.

    Args:
        func (function): The experiment function to run.
        name (str): Name of the experiment.
        run_number (int): Run number of the experiment.
    """
    # stop_event = threading.Event()  # Event to signal when to stop memory logging
    # mem_logger = threading.Thread(target=log_memory_usage, args=(name, run_number, stop_event))  # Memory logging thread
    # mem_logger.start()  # Start the memory logging thread

    start_time = time.time()  # Record the start time
    
    func()  # Run the experiment function
    
    finish_time = time.time()  # Record the finish time
    duration = finish_time - start_time  # Calculate the duration

    # stop_event.set()  # Signal the memory logging thread to stop
    # mem_logger.join()  # Wait for the memory logging thread to finish

    log_results(duration, name, run_number, start_time, finish_time)  # Log the experiment duration

if __name__=='__main__':
    """
    Main entry point for the script. Parses command-line arguments and runs the specified experiment.
    """

    if len(sys.argv) != 4:
        print("Usage: python3 memory_test.py <experiment_name> <run_number>")
        sys.exit(1)

    experiment_name = sys.argv[1]  # Name of the experiment
    run_number = int(sys.argv[2])  # Run number of the experiment
    test_type = sys.argv[3]

    # Ensure the logs directory exists
# Logs will be stored in the "logs/memory_logs" directory relative to the project root
    LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../logs/cpu", test_type))              #"../../../logs/cpu", /app/logs
    os.makedirs(LOG_DIR, exist_ok=True)

    # Map experiment names to their corresponding functions
    function_map = {
        "cpu_low": cpu_low,
        "cpu_medium": cpu_medium,
        "cpu_long": cpu_long
    }

    # Run the specified experiment
    run_experiment(function_map[experiment_name], experiment_name, run_number)