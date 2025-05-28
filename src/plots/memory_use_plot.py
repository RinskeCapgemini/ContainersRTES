import csv
import matplotlib.pyplot as plt
import numpy as np

"""These functions are used to read memory usage from a CSV file and plots the usage"""

def prepare_data(file_path):
    """
    Reads memory usage data from a CSV file, aligns timestamps across runs, and calculates
    the average and standard deviation of memory usage for each timestamp.

    Args:
        file_path (str): Path to the CSV file containing memory usage data.
                         The CSV is expected to have columns: experiment_name, run_number, timestamp, memory_usage.

    Returns:
        tuple: (all_timestamps, average_memory, std_memory)
            - all_timestamps (list of float): Sorted list of all unique timestamps across runs.
            - average_memory (np.ndarray): Average memory usage at each timestamp.
            - std_memory (np.ndarray): Standard deviation of memory usage at each timestamp.
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
    all_timestamps = sorted(set(timestamp for run in runs.values() for timestamp in run["timestamps"]))
    aligned_memory = {run_number: np.interp(all_timestamps, run["timestamps"], run["memory_usage"])
                      for run_number, run in runs.items()}

    # Calculate average and standard deviation
    memory_matrix = np.array(list(aligned_memory.values()))
    average_memory = np.mean(memory_matrix, axis=0)
    std_memory = np.std(memory_matrix, axis=0)

    return all_timestamps, average_memory, std_memory


def plot_memory_usage_side_by_side(file_path_control, file_path_experiment):
    """
    Reads memory usage data from two CSV files (control and experiment), calculates the average and standard deviation
    of memory usage for each, and plots the results side by side for comparison.

    Args:
        file_path_control (str): Path to the control CSV file.
        file_path_experiment (str): Path to the experiment CSV file.

    The function creates a matplotlib plot with two subplots:
        - Left: Control data (average and ±1 std)
        - Right: Experiment data (average and ±1 std)
    """
    control_all_timestamps, control_average_memory, control_std_memory = prepare_data(file_path_control)
    experiment_all_timestamps, experiment_average_memory, experiment_std_memory = prepare_data(file_path_experiment)

    # Create subplots for side-by-side graphs
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

    # Plot control data
    axes[0].plot(control_all_timestamps, control_average_memory, color="blue", label="Average Control", linewidth=2)
    axes[0].fill_between(control_all_timestamps, control_average_memory - control_std_memory, control_average_memory + control_std_memory,
                         color="blue", alpha=0.3, label="Fluctuations Control (±1 std)")
    axes[0].set_title("Control Data", fontsize=14)
    axes[0].set_xlabel("Time (s)", fontsize=12)
    axes[0].set_ylabel("Memory Usage (MB)", fontsize=12)
    axes[0].grid(True, linestyle="--", alpha=0.7)

    # Plot experiment data
    axes[1].plot(experiment_all_timestamps, experiment_average_memory, color="orange", label="Average Test", linewidth=2)
    axes[1].fill_between(experiment_all_timestamps, experiment_average_memory - experiment_std_memory, experiment_average_memory + experiment_std_memory,
                         color="orange", alpha=0.3, label="Fluctuations Test (±1 std)")
    axes[1].set_title("Experiment Data", fontsize=14)
    axes[1].set_xlabel("Time (s)", fontsize=12)
    axes[1].grid(True, linestyle="--", alpha=0.7)

    # Add a shared legend
    fig.legend(["Average Control", "Fluctuations Control (±1 std)", "Average Test", "Fluctuations Test (±1 std)"], loc="upper center", ncol=2, fontsize=12)

    # Adjust layout to make space for the legend
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Filepath to the CSV files -> change based on experiment
    file_path_control = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\adapted_logs\control\memory_medium_usage.csv"
    file_path_experiment = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\adapted_logs\experiment\memory_medium_usage.csv"

    # Call the function to plot the data
    plot_memory_usage_side_by_side(file_path_control, file_path_experiment)