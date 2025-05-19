import csv
import matplotlib.pyplot as plt
import numpy as np


def prepare_data(file_path):
    """Reads io usage data from a CSV file, aligns timestamps across runs, """

    runs = {}  # Dictionary to store data for each run

    # Read the CSV file
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header row

        for row in reader:
            experiment_name, run_number, timestamp, read_usage, write_usage = row
            run_number = int(run_number)
            timestamp = float(timestamp)
            read_usage = float(read_usage)
            write_usage = float(write_usage)

            # Group data by run number
            if run_number not in runs:
                runs[run_number] = {"timestamps": [], "read_speed": [], "write_speed": []}
            runs[run_number]["timestamps"].append(timestamp)
            runs[run_number]["read_speed"].append(read_usage)
            runs[run_number]["write_speed"].append(write_usage)

    # Align timestamps across runs
    all_timestamps = sorted(set(ts for run in runs.values() for ts in run["timestamps"]))
    aligned_read_usage = {run_number: np.interp(all_timestamps, run["timestamps"], run["read_speed"])
                        for run_number, run in runs.items()}
    
    aligned_write_usage = {run_number: np.interp(all_timestamps, run["timestamps"], run["write_speed"])
                    for run_number, run in runs.items()}


    # Calculate average and standard deviation
    read_matrix = np.array(list(aligned_read_usage.values()))
    average_read = np.mean(read_matrix, axis=0)
    std_read = np.std(read_matrix, axis=0)

    # Calculate average and standard deviation
    write_matrix = np.array(list(aligned_write_usage.values()))
    average_write = np.mean(write_matrix, axis=0)
    std_write = np.std(write_matrix, axis=0)

    return all_timestamps, average_read, std_read, average_write, std_write


def prepare_data_for_iteration(file_path, iteration):
    """
    Reads IO usage data from a CSV file and processes data for a specific iteration.

    Args:
        file_path (str): Path to the CSV file.
        iteration (int): The iteration (run number) to process.

    Returns:
        tuple: Timestamps, read usage, and write usage for the specified iteration.
    """
    timestamps = []
    read_usage = []
    write_usage = []

    # Read the CSV file
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header row

        for row in reader:
            experiment_name, run_number, timestamp, read, write = row
            run_number = int(run_number)
            timestamp = float(timestamp)
            read = float(read)
            write = float(write)

            # Process only the specified iteration
            if run_number == iteration:
                timestamps.append(timestamp)
                read_usage.append(read)
                write_usage.append(write)

    return timestamps, read_usage, write_usage


def plot_io_usage_side_by_side(file_path_control, file_path_experiment):
    control_all_timestamps, control_average_read, control_std_read, control_average_write, control_std_write  = prepare_data(file_path_control)
    experiment_all_timestamps, experiment_average_read, experiment_std_read, experiment_average_write, experiment_std_write = prepare_data(file_path_experiment)
    

    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

    # Plot control data
    axes[0].plot(control_all_timestamps, control_average_read, color="blue", label="Average Control", linewidth=2)
    axes[0].fill_between(control_all_timestamps, control_average_read - control_std_read, control_average_read + control_std_read,
                         color="blue", alpha=0.3, label="Fluctuations Control (±1 std)")
    axes[0].set_title("Control Data", fontsize=14)
    axes[0].set_xlabel("Time (s)", fontsize=12)
    axes[0].set_ylabel("read Usage (MB)", fontsize=12)
    axes[0].grid(True, linestyle="--", alpha=0.7)

    axes[0].plot(control_all_timestamps, control_average_write, color="orange", label="Average Control", linewidth=2)
    axes[0].fill_between(control_all_timestamps, control_average_write - control_std_write, control_average_write + control_std_write,
                         color="orange", alpha=0.3, label="Fluctuations Control (±1 std)")
    axes[0].set_title("Control Data", fontsize=14)
    axes[0].set_xlabel("Time (s)", fontsize=12)
    axes[0].set_ylabel("Usage (MB)", fontsize=12)
    axes[0].grid(True, linestyle="--", alpha=0.7)



    # Plot experiment data
    axes[1].plot(experiment_all_timestamps, experiment_average_read, color="blue", label="Average Test", linewidth=2)
    axes[1].fill_between(experiment_all_timestamps, experiment_average_read - experiment_std_read, experiment_average_read + experiment_std_read,
                         color="blue", alpha=0.3, label="Fluctuations Test (±1 std)")
    axes[1].set_title("Experiment Data", fontsize=14)
    axes[1].set_xlabel("Time (s)", fontsize=12)
    axes[1].grid(True, linestyle="--", alpha=0.7)

    axes[1].plot(experiment_all_timestamps, experiment_average_write, color="orange", label="Average experiment", linewidth=2)
    axes[1].fill_between(experiment_all_timestamps, experiment_average_write - experiment_std_write, experiment_average_write + experiment_std_write,
                         color="orange", alpha=0.3, label="Fluctuations experiment (±1 std)")
    axes[1].set_title("Experiment Data", fontsize=14)
    axes[1].set_xlabel("Time (s)", fontsize=12)
    axes[1].set_ylabel("Usage (MB)", fontsize=12)
    axes[1].grid(True, linestyle="--", alpha=0.7)

    # Add a shared legend above the graphs
    fig.legend(["Average Control", "Fluctuations Control (±1 std)", "Average Test", "Fluctuations Test (±1 std)"], 
               loc="upper center", ncol=2, fontsize=12, bbox_to_anchor=(0.5, 1.1))

    # Adjust layout to make space for the legend
    plt.tight_layout(rect=[0, 0, 1, 0.9])

    # Show the plot
    plt.show()


def plot_io_usage_for_iteration(file_path_control, file_path_experiment, iteration):
    """
    Plots IO usage data for a specific iteration from control and experiment files.

    Args:
        file_path_control (str): Path to the control CSV file.
        file_path_experiment (str): Path to the experiment CSV file.
        iteration (int): The iteration (run number) to process.
    """
    # Prepare data for the specified iteration
    control_timestamps, control_read, control_write = prepare_data_for_iteration(file_path_control, iteration)
    experiment_timestamps, experiment_read, experiment_write = prepare_data_for_iteration(file_path_experiment, iteration)

    # Create the plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

    # Plot control data
    axes[0].plot(control_timestamps, control_write, color="orange", label="Write Usage (Control)", linewidth=2, zorder=1)
    axes[0].plot(control_timestamps, control_read, color="blue", label="Read Usage (Control)", linewidth=2, zorder=2)
    axes[0].set_title(f"Control Data (Iteration {iteration})", fontsize=14)
    axes[0].set_xlabel("Time (s)", fontsize=12)
    axes[0].set_ylabel("Usage (MB)", fontsize=12)
    axes[0].grid(True, linestyle="--", alpha=0.7)
    axes[0].set_xlim(left=0)  # Ensure x-axis starts at 0

    # Plot experiment data
    axes[1].plot(experiment_timestamps, experiment_write, color="orange", label="Write Usage (Experiment)", linewidth=2, zorder=1)
    axes[1].plot(experiment_timestamps, experiment_read, color="blue", label="Read Usage (Experiment)", linewidth=2, zorder=2)
    axes[1].set_title(f"Experiment Data (Iteration {iteration})", fontsize=14)
    axes[1].set_xlabel("Time (s)", fontsize=12)
    axes[1].grid(True, linestyle="--", alpha=0.7)
    axes[1].set_xlim(left=0)  # Ensure x-axis starts at 0

    # Add a shared legend above the graphs
    fig.legend(["Read Usage (Control)", "Write Usage (Control)", "Read Usage (Experiment)", "Write Usage (Experiment)"], 
               loc="upper center", ncol=2, fontsize=12, bbox_to_anchor=(0.5, 0.95))  # Lowered the legend

    # Adjust layout to make space for the legend
    plt.tight_layout(rect=[0, 0, 1, 0.8])  # Increased space for the legend

    # Show the plot
    plt.show()


# File paths to the CSV files
file_path_control = r"c:\Users\RHEEREN\GitHub\logs\io_logs\i1\control\io_long_speed.csv"
file_path_experiment = r"c:\Users\RHEEREN\GitHub\logs\io_logs\i1\experiment\io_long_speed.csv"

# Specify the iteration to process
# for iteration in range(9):

    # Plot IO usage for the specified iteration
plot_io_usage_for_iteration(file_path_control, file_path_experiment, 0)