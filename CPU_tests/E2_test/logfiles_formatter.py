import os
import csv
import pandas as pd

# Folder containing csv files
folder_path = "long_container/log_files"
output_csv = "long_container/container_logs.csv"

# Calculate average total time
def calculate_average(csv):
    df = pd.read_csv(csv)
    return df["total_time"].mean()

# Time formatting function
def to_seconds(timestamp):
    return int(timestamp) / 1e9

# Open CSV file to write

with open(output_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["container_id", "started", "finished", "total_time"])

    # Loop through files in folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            container_id = filename.replace(".txt", "")

            with open(os.path.join(folder_path, filename), "r") as file:
                lines = file.readlines()
                started = to_seconds(lines[0].split(": ")[1].strip())
                finished = to_seconds(lines[1].split(": ")[1].strip())
                total_time = finished - started
                
                writer.writerow([container_id, started, finished, total_time])

print(f"CSV-file '{output_csv}' created.")

# Average total time
print(f"Average time {calculate_average(output_csv)}")