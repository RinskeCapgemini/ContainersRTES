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
            continue  # skip this line
        elif line.startswith("Average"):
            continue  # skip averages
        elif line:
            try:
                value = float(line)
                data[current_experiment].append(value)
            except ValueError:
                pass  # ignore non-numeric lines
    return data

# Filenames (adjust paths if needed)
files = {
    "container3_engine3": "log_files/container3_engine3.txt",
    "control": "log_files/control.txt",
    "engine2_container3": "log_files/engine2_container3.txt"
}

# Read data from all files
all_data = {}
for name, path in files.items():
    all_data[name] = read_experiment_data(path)

# Function to plot one experiment dataset
def plot_experiment(data_dict, title):
    plt.figure(figsize=(10, 5))
    for test_name, values in data_dict.items():
        plt.plot(range(1, len(values)+1), values, marker='o', label=test_name)
    plt.title(title)
    plt.xlabel("Measurement")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    # plt.legend()
    plt.tight_layout()
    plt.show()

# Plot each dataset
for name, dataset in all_data.items():
    plot_experiment(dataset, f"Results from {name}")
