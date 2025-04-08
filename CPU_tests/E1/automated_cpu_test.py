import time
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CPU_calculation_scripts.simple_calculation import *
from CPU_calculation_scripts.medium_calculation import *
from CPU_calculation_scripts.long_calculation import *

def log_results(time_list, experiment_name, file_name):
    average = sum(time_list) / len(time_list)

    with open(f"{file_name}.txt",'a') as log_file:
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

    run_experiment(simple_calc, "Simple CPU")     
    run_experiment(mid_calc, "Mid CPU")
    run_experiment(long_calc, "Long CPU")
