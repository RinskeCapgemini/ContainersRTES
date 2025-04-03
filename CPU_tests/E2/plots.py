import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
data = pd.read_csv('medium_container/container_logs.csv')

# Assuming the CSV has a column named 'time'
# Create an index for datapoints (from 1 to number of rows)
datapoints = range(1, len(data) + 1)
time_values = data['total_time']

# Plot the time distribution for each datapoint
plt.figure(figsize=(10, 6))
plt.plot(datapoints, time_values, marker='o', linestyle='-', color='b')
plt.xlabel('Datapoints')
plt.ylabel('Time')
plt.title('Time Distribution for Each Datapoint')
plt.grid(True)
plt.tight_layout()
plt.show()