import matplotlib.pyplot as plt

# Function to read experiment data from a file
def read_experiment_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    data = {}
    current_experiment = None
    for line in lines:
        line = line.strip()
        if line.startswith("Experiment name"):
            current_experiment = line.split(" = ")[1]
            data[current_experiment] = []
        elif line.startswith("Raw data"):
            continue
        elif line.startswith("Average"):
            continue
        elif line:
            try:
                value = float(line)
                data[current_experiment].append(value)
            except ValueError:
                pass
    return data

# File names
files = {
    "control": "log_files/control.txt",
    "engine2_container3": "log_files/engine2_container3.txt",
    "container3_engine3": "log_files/container3_engine3.txt"
   
}

# Read all data
all_data = {name: read_experiment_data(path) for name, path in files.items()}

# Compute averages
averages = {"Simple CPU": {}, "Mid CPU": {}, "Long CPU": {}}

for source_name, experiments in all_data.items():
    for cpu_type in ["Simple CPU", "Mid CPU", "Long CPU"]:
        if cpu_type in experiments:
            measurements = experiments[cpu_type]
            avg = sum(measurements) / len(measurements)
            averages[cpu_type][source_name] = avg

# Colors for consistency
color_map = {
    "container3_engine3": 'tomato',
    "control": 'mediumseagreen',
    "engine2_container3": 'cornflowerblue'
}

# 1. Bar chart for each CPU level
def plot_average_for_cpu(cpu_type, avg_data):
    sources = list(avg_data.keys())
    values = list(avg_data.values())
    colors = [color_map.get(source, 'gray') for source in sources]

    plt.figure(figsize=(7, 5))
    plt.bar(sources, values, color=colors)
    plt.title(f"Average Time - {cpu_type}")
    plt.ylabel("Average Time (seconds)")
    plt.xlabel("Source")
    plt.grid(axis='y')

    # Optional: Add value labels above bars
    for i, v in enumerate(values):
        plt.text(i, v + 0.5, f"{v:.2f}", ha='center', fontweight='bold')

    plt.tight_layout()
    plt.show()

# 2. Line graph comparing all CPU levels per source
def plot_all_cpu_averages(averages):
    cpu_types = list(averages.keys())
    sources = list(next(iter(averages.values())).keys())

    plt.figure(figsize=(10, 6))
    for source in sources:
        values = [averages[cpu][source] for cpu in cpu_types]
        plt.plot(cpu_types, values, marker='o', label=source, color=color_map.get(source, 'gray'))

    plt.title("Average Task Time per CPU Type (All Sources)")
    plt.xlabel("CPU Type")
    plt.ylabel("Average Time (seconds)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Plot each CPU type as a separate bar chart
for cpu_type in ["Simple CPU", "Mid CPU", "Long CPU"]:
    plot_average_for_cpu(cpu_type, averages[cpu_type])

# Plot combined line graph
plot_all_cpu_averages(averages)
