import pandas as pd
import matplotlib.pyplot as plt

csv_file = "log_files/container_performance.csv"

data_file = pd.read_csv(csv_file)

data_file["timestamp"] = pd.to_datetime(data_file["timestamp"])

plt.figure(figsize=(10,5))
# plt.plot(data_file["timestamp"], data_file["runtime_ms"], marker='o', linestyle='-')
plt.plot(data_file["runtime_ms"], data_file["active_containers"], marker='o', linestyle='-')

plt.xlabel("Time")
plt.ylabel("Runtime (ms)")
plt.title("Container Runtime Over Time")
plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.show()