import csv
import math

"""Calculate the average runtime and standard deviation for the program runtime."""

def calculate_average_runtime(file_path):
    """
    Calculates the average runtime from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        float: Average runtime in seconds.
    """
    total_runtime = 0.0
    count = 0

    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header row

        for row in reader:
            # Extract the runtime from the "Duration (s)" column
            runtime = float(row[4])  # Column index 4 corresponds to "Duration (s)"
            total_runtime += runtime
            count += 1

    # Calculate the average runtime
    average_runtime = total_runtime / count if count > 0 else 0.0
    return average_runtime


def calculate_standard_deviation(file_path, average_runtime):
    """
    Calculates the standard deviation of runtimes from a CSV file.

    Args:
        file_path (str): Path to the CSV file.
        average_runtime (float): The average runtime.

    Returns:
        float: Standard deviation of runtimes in seconds.
    """
    squared_diff_sum = 0.0
    count = 0

    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header row

        for row in reader:
            # Extract the runtime from the "Duration (s)" column
            runtime = float(row[4])  # Column index 4 corresponds to "Duration (s)"
            squared_diff_sum += (runtime - average_runtime) ** 2
            count += 1

    # Calculate the standard deviation
    standard_deviation = math.sqrt(squared_diff_sum / count) if count > 0 else 0.0
    return standard_deviation


# File path to the CSV file
file_path = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\cache_testing\experiment\memory_medium_time.csv"

# Calculate the average runtime
average_runtime = calculate_average_runtime(file_path)

# Calculate the standard deviation
standard_deviation = calculate_standard_deviation(file_path, average_runtime)

# Print the results
print(f"Average Runtime: {average_runtime:.5f} seconds")
print(f"Standard Deviation: {standard_deviation:.5f} seconds")