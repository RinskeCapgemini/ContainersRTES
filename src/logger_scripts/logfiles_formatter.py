import os
import csv
import pandas as pd

# Folder containing the log files and output CSV file path
folder_path = "long_container/log_files"
output_csv = "long_container/container_logs.csv"

# Calculate average total time
def calculate_average(csv_file):
    df = pd.read_csv(csv_file)
    return df["total_time"].mean()

# Convert timestamp from nanoseconds (as integer string) to seconds (float)
def to_seconds(timestamp):
    return int(timestamp) / 1e9

# Gather container data in a list
container_data = []

# Loop through files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        container_id = filename.replace(".txt", "")
        with open(os.path.join(folder_path, filename), "r") as file:
            lines = file.readlines()
            # Expecting lines formatted like: "started: <timestamp>" and "finished: <timestamp>"
            started = to_seconds(lines[0].split(": ")[1].strip())
            finished = to_seconds(lines[1].split(": ")[1].strip())
            total_time = finished - started
            container_data.append([container_id, started, finished, total_time])

# Sort the data based on the start time (second element)
container_data.sort(key=lambda x: x[1])

# Write the sorted data to CSV
with open(output_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["container_id", "started", "finished", "total_time"])
    writer.writerows(container_data)

print(f"CSV file '{output_csv}' created.")
print(f"Average time {calculate_average(output_csv)}")
