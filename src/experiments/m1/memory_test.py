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

def log_results(time_list, experiment_name):
    average = sum(time_list) / len(time_list)

    log_path = os.path.join(LOG_DIR,  f"{experiment_name}_time.csv")

    # Write results to a CSV file
    with open(log_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write the header if the file is empty
        if os.stat(log_path).st_size == 0:
            writer.writerow(["Experiment Name", "Run Number", "Duration (s)"])
        
        # Write each runtime to the CSV
        for i, runtime in enumerate(time_list, start=1):
            writer.writerow([experiment_name, i, runtime])
        
        # Write the average runtime as a summary row
        writer.writerow([experiment_name, "Average", average])

        
def log_memory_usage(experiment_name, stop_event):
    process = psutil.Process(os.getpid())
    memory_log_path = os.path.join(LOG_DIR, f"{experiment_name}_usage.csv")

    with open(memory_log_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write header if file is empty
        if os.stat(memory_log_path).st_size == 0:
            writer.writerow(["Experiment Name", "Timestamp (s)", "Memory Usage (MB)"])

        start_time = time.time()

        writer.writerow(["-", "-", "-"]) 

        while not stop_event.is_set():
            mem_usage_mb = process.memory_info().rss / 1024 / 1024
            timestamp = time.time() - start_time
            writer.writerow([experiment_name, f"{timestamp:.2f}", f"{mem_usage_mb:.2f}"])
            time.sleep(0.1)


def run_experiment(func, name):
    runtimes = []

    # for i in range(runs):
    stop_event = threading.Event()
    mem_logger = threading.Thread(target=log_memory_usage, args=(name, stop_event))
    mem_logger.start()

    start_time = time.time()
    func()
    duration = time.time() - start_time
    runtimes.append(duration)

    stop_event.set()
    mem_logger.join()

    log_results(runtimes, name)



if __name__=='__main__':

    run_experiment(memory_low, "memory_low")     
    print("Done with experiment low")

    # run_experiment(memory_medium, "memory_medium")
    # print("Done with experiment medium")

    # run_experiment(memory_long, "memory_long")
    # print("Done with experiment long")
