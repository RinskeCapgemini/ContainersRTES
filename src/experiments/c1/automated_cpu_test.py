import time
import os
import sys

# Add the cpu_calculations folder to the Python path
cpu_calculations_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../cpu_calculations'))
sys.path.append(cpu_calculations_path)

# Import the calculation modules
from long_calculation import LongCalculation
from medium_calculation import MediumCalculation
from simple_calculation import SimpleCalculation

LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(LOG_DIR, exist_ok=True)  # Make sure the directory exists

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

    run_experiment(SimpleCalculation.simple_calc, "Simple CPU")     
    run_experiment(MediumCalculation.mid_calc, "Mid CPU")
    run_experiment(LongCalculation.long_calc, "Long CPU")
