import csv
from datetime import datetime
import matplotlib.pyplot as plt

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

def plot_stacked_bar(average_times_1, average_times_2, average_total, labels):
    """
    Plots the average times as a stacked bar graph with total time displayed above each bar.

    Args:
        average_times_1 (list): List of average durations for the first layer (e.g., timestamp times).
        average_times_2 (list): List of average durations for the second layer (e.g., outside times).
        labels (list): List of labels for the bars.
    """
    plt.figure(figsize=(8, 6))
    bar_width = 0.5

    # Plot the first layer (timestamp times)
    plt.bar(labels, average_times_1, color='blue', label='Timestamp Time', width=bar_width)

    # Plot the second layer (outside times) stacked on top
    plt.bar(labels, average_times_2, bottom=average_times_1, color='orange', label='Outside Time', width=bar_width)

    # Add total time above each bar
    # Display total time above the single bar

    # Add total time inside the bar
    plt.text(0, average_total / 2, f"{average_total:.2f}s", ha='center', va='center', fontsize=10, color='white')    
    
    # Add labels, title, and legend
    plt.xlabel("Files", fontsize=12)
    plt.ylabel("Average Duration (s)", fontsize=12)
    plt.title("Average Duration Comparison (Stacked)", fontsize=14)
    plt.legend(loc="upper left")
    plt.grid(axis='y', linestyle="--", alpha=0.7)

    # Show the plot
    plt.tight_layout()
    plt.show()

# File paths
short_inside_times = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\experiment\memory_short_time.csv"
short_outside_times = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\experiment\memory_short_outside_time.csv"

mid_inside_times = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\experiment\memory_medium_time.csv"
mid_outside_times = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\experiment\memory_medium_outside_time.csv"

long_inside_times = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\experiment\memory_long_time.csv"
long_outside_times = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\experiment\memory_long_outside_time.csv"

# Calculate average times
average_long_i = calculate_average_time(long_inside_times, time_format='timestamp')
average_long_o = calculate_average_time(long_outside_times, time_format='datetime')

# Prepare data for stacked bar plot
average_times_long = [average_long_o]  # Bottom layer
average_diff_long = [average_long_i - average_long_o]  # Top layer (difference)

# Plot the results
plot_stacked_bar(average_long_i, average_diff_long, average_long_o, ["Memory Long"])
