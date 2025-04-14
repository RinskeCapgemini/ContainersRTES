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
os.makedirs("../../../logs", exist_ok=True)

output_file = "../../../logs/memory_usage_low.csv"          # Change name according to test being performed

timestamps = []
memory_usage = []
_running = False
_start_time = None

process = psutil.Process(os.getpid())

def start_tracking(output_file, interval=0.05):
    global _running, _start_time

    _running = True
    _start_time = time.time()

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time_sec', 'memory_MB'])
        while _running:
            current_time = time.time() - _start_time
            mem_usage = process.memory_info().rss / (1024 * 1024)
            writer.writerow([current_time, mem_usage])
            timestamps.append(current_time)
            memory_usage.append(mem_usage)
            time.sleep(interval)

def stop_tracking():
    global _running
    _running = False

def get_peak_memory():
    return max(memory_usage) if memory_usage else 0

def get_memory_data():
    return timestamps, memory_usage

if __name__ == "__main__":
    # Start tracking memory usage
    tracking_thread = psutil.Process(os.getpid())
    start_tracking(output_file)

    # Run memory tests
    for i in range(10):
        memory_low()

        # memory_medium()

        # memory_long()

    # Stop tracking memory usage
    stop_tracking()

    # Output peak memory usage
    peak_memory = get_peak_memory()
    print(f"Peak memory usage: {peak_memory:.2f} MB")



