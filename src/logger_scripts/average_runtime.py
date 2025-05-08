import csv

"""Calcuate the average runtime for the program runtime ."""

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

# File path to the CSV file
file_path = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m2\control\memory_long_time.csv"

# Calculate the average runtime
average_runtime = calculate_average_runtime(file_path)

# Print the result
print(f"Average Runtime: {average_runtime:.5f} seconds")