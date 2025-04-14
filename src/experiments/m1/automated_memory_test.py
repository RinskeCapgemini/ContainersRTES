import time
import os
import psutil
import sys
import csv

# Add the memory_calculations folder to the Python path
memory_calculations_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../memory_calculations'))
sys.path.append(memory_calculations_path)

from memory_low import memory_low
from memory_medium import memory_medium
from memory_long import memory_long

# Ensure the logs directory exists
LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../logs/memory_logs"))
os.makedirs("../../../logs", exist_ok=True)

output_file = "../../../logs/memory_logs/memory_usage_low.csv"          # Change name according to test being performed

def log_results(time_list, experiment_name, file_name):
    average = sum(time_list) / len(time_list)

    log_path = os.path.join(LOG_DIR, f"{file_name}.txt")

    with open(log_path,'a') as log_file:
        log_file.write(f"Experiment name = {experiment_name}\n")
        log_file.write(f"Raw data: \n")
        for i in time_list : log_file.write(f"{i}\n")
        log_file.write(f"Average tasktime over x{len(time_list)} = {average}\n")


def run_experiment(func, name, runs=10):
    runtimes = []

    for i in range(runs):
        start_time = time.time()
        func()
        duration = time.time() - start_time
        runtimes.append(duration)
    
    log_results(runtimes, name, file_name="automated_logs")


if __name__=='__main__':

    run_experiment(memory_low, "Simple CPU")     
    run_experiment(memory_medium, "Mid CPU")
    run_experiment(memory_long, "Long CPU")
