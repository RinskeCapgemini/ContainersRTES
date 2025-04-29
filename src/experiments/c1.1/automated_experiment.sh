#!/bin/bash

test_name=$1
test_type=$2 

# Log directories
host_log_dir="/home/rinske/Github/ContainersRTES/logs/cpu_logs/c1/"  # Host directory for logs
container_log_dir="/app/logs"  # Container directory for logs

# Python script directories
host_cpu_test_dir="/home/rinske/Github/ContainersRTES/src/experiments/c1.1"  # Directory containing cpu_test.py
host_cpu_calculations_dir="/home/rinske/Github/ContainersRTES/src/cpu_calculations"  # Directory containing cpu calculation scripts

# CSV file to store experiment data
csv_file="${host_log_dir}experiment/${test_name}_outside_time.csv"

# Add CSV header if the file doesn't exist
if [ ! -f "$csv_file" ]; then
    echo "Experiment Name,Run Number,Start Time,Finish Time" > "$csv_file"
fi


# sudo docker run --cpuset-cpus=3 -v /home/rinske/Github/ContainersRTES/CPU_tests/E1/log_files:/app/logs e1:1.0

# for i in {0..9}; do
# Log the start time
start_time=$(date '+%Y-%m-%d %H:%M:%S.%N')  # Human-readable time with nanoseconds

# Run the Docker container with volume mappings for logs and scripts
sudo docker run --cpuset-cpus=3 --rm \
    -v "$host_log_dir:$container_log_dir" \
    -v "$host_cpu_test_dir:/app/experiments/c1" \
    -v "$host_cpu_calculations_dir:/app/cpu_calculations" \
    general_container:1.0 /app/experiments/c1/cpu_test.py $test_name $i $test_type

# Log the finish time
finish_time=$(date '+%Y-%m-%d %H:%M:%S.%N')  # Human-readable time with nanoseconds

# Append the data to the CSV file
echo "$test_name,$i,$start_time,$finish_time" >> "$csv_file"


# done