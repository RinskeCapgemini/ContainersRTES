#!/bin/bash

# Run with sudo 

test_name=$1

# Log directories
host_log_dir="/home/rinske/Github/ContainersRTES/logs/memory_logs/m2/"  # Host directory for logs
container_log_dir="/app/logs"  # Container directory for logs

# Python script directories
host_memory_test_dir="/home/rinske/Github/ContainersRTES/src/experiments/m2"  # Directory containing memory_test.py
host_memory_calculations_dir="/home/rinske/Github/ContainersRTES/src/memory_calculations"  # Directory containing memory calculation scripts

# CSV file to store experiment data
csv_file="${host_log_dir}experiment/${test_name}_container_time.csv"

# Add CSV header if the file doesn't exist
if [ ! -f "$csv_file" ]; then
    echo "Experiment Name,Run Number,Start Time,Finish Time" > "$csv_file"
fi


for i in {0..9}; do
    # Log the start time
    start_time=$(date '+%Y-%m-%d %H:%M:%S.%N')  # Human-readable time with nanoseconds
    
    # Run the Docker container with volume mappings for logs and scripts
    sudo docker run --rm \
        -v "$host_log_dir:$container_log_dir" \
        -v "$host_memory_test_dir:/app/experiments/m2" \
        -v "$host_memory_calculations_dir:/app/memory_calculations" \
        general_container:1.0 /app/experiments/m2/memory_test.py $test_name $i experiment

    # Log the finish time
    finish_time=$(date '+%Y-%m-%d %H:%M:%S.%N')  # Human-readable time with nanoseconds

    # Append the data to the CSV file
    echo "$test_name,$i,$start_time,$finish_time" >> "$csv_file"


done

sudo unmount /mnt/usb