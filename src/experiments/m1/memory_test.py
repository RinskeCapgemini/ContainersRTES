import time
import os
import psutil
import sys
import csv
import threading

# Add the memory_calculations folder to the Python path
memory_calculations_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../memory_calculations'))
sys.path.append(memory_calculations_path)

from memory_low import memory_low
from memory_medium import memory_medium
from memory_long import memory_long

# Ensure the logs directory exists
LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../logs/memory_logs"))
os.makedirs(LOG_DIR, exist_ok=True)

def log_results(duration, experiment_name, run_number):
    log_path = os.path.join(LOG_DIR, f"{experiment_name}_time.csv")

    with open(log_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if os.stat(log_path).st_size == 0:
            writer.writerow(["Experiment Name", "Run Number", "Duration (s)"])

        writer.writerow([experiment_name, run_number, duration])


        
def log_memory_usage(experiment_name, stop_event):
    process = psutil.Process(os.getpid())
    memory_log_path = os.path.join(LOG_DIR, f"{experiment_name}_usage.csv")

    with open(memory_log_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if os.stat(memory_log_path).st_size == 0:
            writer.writerow(["Experiment Name", "Timestamp (s)", "Memory Usage (MB)"])

        start_time = time.time()

        while not stop_event.is_set():
            mem_usage_mb = process.memory_info().rss / 1024 / 1024
            timestamp = time.time() - start_time
            writer.writerow([experiment_name, f"{timestamp:.2f}", f"{mem_usage_mb:.2f}"])
            time.sleep(0.1)


def run_experiment(func, name, run_number):
    run_id = f"{name}_run{run_number}"
    stop_event = threading.Event()
    mem_logger = threading.Thread(target=log_memory_usage, args=(run_id, stop_event))
    mem_logger.start()

    start_time = time.time()
    func()
    duration = time.time() - start_time

    stop_event.set()
    mem_logger.join()

    log_results(duration, name, run_number)


if __name__=='__main__':

    if len(sys.argv) != 3:
        print("Usage: python3 memory_test.py <experiment_name> <run_number>")
        sys.exit(1)

    experiment_name = sys.argv[1]
    run_number = int(sys.argv[2])

    function_map = {
        "memory_low": memory_low,
        "memory_medium": memory_medium,
        "memory_long": memory_long
    }

    run_experiment(function_map[experiment_name], experiment_name, run_number)