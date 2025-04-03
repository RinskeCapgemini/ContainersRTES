import subprocess
import os
import csv
from datetime import datetime
import pandas as pd


logger_path = "log_files"
output_file = "container_outside_logs.csv"

def to_seconds(timestamp):
    dt = datetime.strptime(timestamp.rstrip("Z"), "%Y-%m-%dT%H:%M:%S.%f")
    return dt.timestamp()  # Convert to seconds since epoch

def get_container_ids():
    container_ids = []

    for filename in os.listdir(logger_path):
        if filename.endswith(".txt"):
            container_id = filename.replace(".txt", "")
            container_ids.append(container_id)

    return container_ids

def container_times(container_id):
    start_time = subprocess.check_output(["docker", "inspect", "-f", "{{.State.StartedAt}}", container_id]).decode().strip()
    start_time = to_seconds(start_time)
    stop_time = subprocess.check_output(["docker", "inspect", "-f", "{{.State.FinishedAt}}", container_id]).decode().strip()
    stop_time = to_seconds(stop_time)
    
    return start_time, stop_time


# Calculate average total time
def calculate_average(csv):
    df = pd.read_csv(csv)
    return df["total_time"].mean()

if __name__=='__main__':
    contianer_ids = get_container_ids()

    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["container_id", "started", "finished", "total_time"])

        for id in contianer_ids:
            start, stop = container_times(id)

            total = stop - start

            writer.writerow([id, start, stop, total])

    print(f"Average time {calculate_average(output_file)}")

    