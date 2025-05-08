import pandas as pd
import matplotlib.pyplot as plt

# File paths for control and experiment data
control_file = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\adapted_logs\control\memory_long_usage.csv"
experiment_file = r"c:\Users\RHEEREN\GitHub\logs\memory_logs\m1\adapted_logs\experiment\memory_long_usage.csv"

def calculate_average_memory_by_timestamp(file_path):
    """
    Groups the data by Timestamp (s) and calculates the average memory usage for each timestamp.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame with Timestamp (s) and average memory usage.
    """
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Group by Timestamp (s) and calculate the average memory usage
    avg_memory_by_timestamp = df.groupby("Timestamp (s)")["Memory Usage (MB)"].mean().reset_index()

    return avg_memory_by_timestamp

def plot_average_memory(control_avg, experiment_avg):
    """
    Plots the average memory usage for control and experiment data grouped by timestamp.

    Args:
        control_avg (pd.DataFrame): DataFrame with control average memory usage by timestamp.
        experiment_avg (pd.DataFrame): DataFrame with experiment average memory usage by timestamp.
    """
    plt.figure(figsize=(10, 6))

    # Plot control data
    plt.plot(control_avg["Timestamp (s)"], control_avg["Memory Usage (MB)"], label="Control", color="blue", marker="o")

    # Plot experiment data
    plt.plot(experiment_avg["Timestamp (s)"], experiment_avg["Memory Usage (MB)"], label="Experiment", color="orange", marker="o")

    # Add labels, title, and legend
    plt.xlabel("Timestamp (s)", fontsize=12)
    plt.ylabel("Average Memory Usage (MB)", fontsize=12)
    plt.title("Average Memory Usage by Timestamp", fontsize=14)
    plt.legend()
    plt.grid(alpha=0.5)

    # Show the plot
    plt.tight_layout()
    plt.show()

# Calculate average memory usage by timestamp for control and experiment
control_avg = calculate_average_memory_by_timestamp(control_file)
experiment_avg = calculate_average_memory_by_timestamp(experiment_file)

# Plot the results
plot_average_memory(control_avg, experiment_avg)