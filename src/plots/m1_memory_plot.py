import csv
import matplotlib.pyplot as plt
import numpy as np

def plot_memory_usage_with_average(file_path):
    """
    Reads memory usage data from a CSV file, calculates the average memory usage across runs,
    and plots only the average with fluctuations.

    Args:
        file_path (str): Path to the CSV file.
    """
    runs = {}  # Dictionary to store data for each run

    # Read the CSV file
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header row

        for row in reader:
            experiment_name, run_number, timestamp, memory_usage = row
            run_number = int(run_number)
            timestamp = float(timestamp)
            memory_usage = float(memory_usage)

            # Group data by run number
            if run_number not in runs:
                runs[run_number] = {"timestamps": [], "memory_usage": []}
            runs[run_number]["timestamps"].append(timestamp)
            runs[run_number]["memory_usage"].append(memory_usage)

    # Align timestamps across runs
    all_timestamps = sorted(set(ts for run in runs.values() for ts in run["timestamps"]))
    aligned_memory = {run_number: np.interp(all_timestamps, run["timestamps"], run["memory_usage"])
                      for run_number, run in runs.items()}

    # Calculate average and standard deviation
    memory_matrix = np.array(list(aligned_memory.values()))
    average_memory = np.mean(memory_matrix, axis=0)
    std_memory = np.std(memory_matrix, axis=0)

    # Plot the average with a shaded region for standard deviation
    plt.figure(figsize=(10, 6))
    plt.plot(all_timestamps, average_memory, color="blue", label="Average", linewidth=2)  # Vibrant blue for the average
    plt.fill_between(all_timestamps, average_memory - std_memory, average_memory + std_memory,
                     color="orange", alpha=0.3, label="Fluctuations (±1 std)")  # Orange for the fluctuations

    # Add labels, title, and legend
    plt.xlabel("Time (s)", fontsize=12, color="black")
    plt.ylabel("Memory Usage (MB)", fontsize=12, color="black")
    plt.title("Memory Usage Over Time (Average and Fluctuations)", fontsize=14, color="black")
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))  # Move legend to the right of the plot
    plt.grid(True, linestyle="--", alpha=0.7)

    # Adjust layout to make space for the legend
    plt.tight_layout(rect=[0, 0, 0.85, 1])

    # Show the plot
    plt.show()

# Filepath to the CSV file
file_path = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\control\memory_long_usage.csv"

# Call the function to plot the data
plot_memory_usage_with_average(file_path)