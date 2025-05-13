import csv
import matplotlib.pyplot as plt
import numpy as np


def plot_separate_graphs(file_path):
    """
    Reads the average runtime data from a CSV file and plots separate bar graphs for each entry.

    Args:
        file_path (str): Path to the CSV file.
    """
    # Read the CSV file
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header row

        for row in reader:
            entry = row[0]  # Entry name (e.g., simple, medium, long)
            control_time = float(row[1])  # Control time
            program_time = float(row[2])  # Program time
            container_time = float(row[3])  # Container time

            surplus_time = container_time - program_time

            # Create a bar graph for the current entry
            plt.figure(figsize=(6, 4))

            # Plot control time
            plt.bar("Control", control_time, color='blue')
            plt.text(0, control_time + 0.5, f"{control_time:.2f}s", ha='center', va='bottom', fontsize=10)

            # Plot program time stacked with container time
            plt.bar("Program + Container", program_time, color='blue')
            plt.bar("Program + Container", surplus_time, bottom=program_time, color='orange')
            plt.text(1, program_time + surplus_time + 0.5, f"{program_time + surplus_time:.2f}s", ha='center', va='bottom', fontsize=10)

            # Extend the y-axis to create space above the bars
            plt.ylim(0, max(control_time, program_time + surplus_time) * 1.5)

            # Add labels, title, and legend
            plt.ylabel("Time (s)", fontsize=12)
            plt.title(f"Average Runtime for {entry.capitalize()}", fontsize=14)
            plt.legend(loc="upper left")
            plt.grid(axis='y', linestyle="--", alpha=0.7)

            # Show the plot
            # plt.tight_layout()
            plt.show()


# File path to the CSV file
file_path = r"c:\Users\RHEEREN\GitHub\logs\io_logs\i1\average.csv"

# Plot separate graphs for each entry
plot_separate_graphs(file_path)

