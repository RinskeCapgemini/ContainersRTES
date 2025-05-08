import csv
from datetime import datetime
import os

def calculate_average_time(file_path, time_format):
    """
    Calculates the average duration from a CSV file.

    Args:
        file_path (str): Path to the CSV file.
        time_format (str): Format of the time in the file ('timestamp' or 'datetime').

    Returns:
        float: Average duration in seconds.
    """
    durations = []

    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header row

        for row in reader:
            if time_format == 'timestamp':
                start_time = float(row[2])
                finish_time = float(row[3])
            elif time_format == 'datetime':
                # Truncate nanoseconds to microseconds
                start_time = datetime.strptime(row[2][:26], "%Y-%m-%d %H:%M:%S.%f")
                finish_time = datetime.strptime(row[3][:26], "%Y-%m-%d %H:%M:%S.%f")
                start_time = start_time.timestamp()
                finish_time = finish_time.timestamp()
            else:
                raise ValueError("Invalid time format. Use 'timestamp' or 'datetime'.")

            duration = finish_time - start_time
            durations.append(duration)

    return sum(durations) / len(durations) if durations else 0

def process_all_logs(folder_path):
    """
    Processes all time log files in the folder and calculates their average durations.

    Args:
        folder_path (str): Path to the folder containing the log files.
    """
    time_files = [f for f in os.listdir(folder_path) if f.endswith("_time.csv")]
    results = {}

    for file_name in time_files:
        file_path = os.path.join(folder_path, file_name)

        # Determine the time format based on the file content
        with open(file_path, 'r') as csv_file:
            header = csv_file.readline()
            if "Start Time" in header and "Finish Time" in header:
                time_format = 'timestamp' if "Duration" in header else 'datetime'
            else:
                continue

        # Calculate the average time
        average_time = calculate_average_time(file_path, time_format)
        results[file_name] = average_time

    # Print the results
    print("Average Durations (in seconds):")
    for file_name, avg_time in results.items():
        print(f"{file_name}: {avg_time:.5f}s")

# Folder path containing the log files
folder_path = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\control"

# Process all logs and calculate averages
process_all_logs(folder_path)