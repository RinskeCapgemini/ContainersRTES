import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
outside_data = pd.read_csv('medium_container/container_outside_logs.csv')
inside_data = pd.read_csv('medium_container/container_logs.csv')

# Assuming the CSV has a column named 'time'
# Create an index for datapoints (from 1 to number of rows)
datapoints = range(1, len(outside_data) + 1)
outside_values = outside_data['total_time']
inside_values = inside_data['total_time']

# Plot the time distribution for each datapoint
plt.figure(figsize=(10, 6))
plt.plot(datapoints, outside_values, marker='o', linestyle='-', color='b')
plt.plot(datapoints, inside_values, marker='o', linestyle='-', color='r')
plt.xlabel('Datapoints')
plt.ylabel('Time')
plt.title('Time Distribution for Each Datapoint')
plt.grid(True)
plt.tight_layout()
plt.show()