import csv
from datetime import datetime

"""Calculates the total container runtime. Total runtimes are added to the existing csv file, and print average runtime."""


def calculate_total_time(file_path):
    """
    Calculates the total time from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        float: Total time in seconds.
    """
    total_time = 0.0

    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header row

        for row in reader:
            # Parse the start and finish times
            start_time = datetime.strptime(row[2][:26], "%Y-%m-%d %H:%M:%S.%f")
            finish_time = datetime.strptime(row[3][:26], "%Y-%m-%d %H:%M:%S.%f")

            # Calculate the duration and add to the total
            duration = (finish_time - start_time).total_seconds()
            total_time += duration

    return total_time

def append_average_to_csv(file_path):
    """
    Calculates the duration for each row and appends the average duration to the CSV file.

    Args:
        file_path (str): Path to the CSV file.
    """
    rows = []
    total_time = 0.0

    # Read the CSV file and calculate durations
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Read the header row
        header.append("Duration (s)")  # Add a new column for duration
        rows.append(header)

        for row in reader:
            # Parse the start and finish times
            start_time = datetime.strptime(row[2][:26], "%Y-%m-%d %H:%M:%S.%f")
            finish_time = datetime.strptime(row[3][:26], "%Y-%m-%d %H:%M:%S.%f")

            # Calculate the duration
            duration = (finish_time - start_time).total_seconds()
            total_time += duration

            # Append the duration to the row
            row.append(f"{duration:.5f}")
            rows.append(row)

    # Calculate the average duration
    average_duration = total_time / (len(rows) - 1) if len(rows) > 1 else 0.0

    # Write the updated rows back to the CSV file
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)

    print(f"Average Duration: {average_duration:.5f} seconds")

# File path to the CSV file -> Change this to your actual file path
file_path = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\cache_testing\experiment\memory_medium_outside_time.csv"

# Calculate the total time
total_time = calculate_total_time(file_path)

# Print the result
print(f"Total Time: {total_time:.5f} seconds")

# Append the average duration to the CSV file
append_average_to_csv(file_path)