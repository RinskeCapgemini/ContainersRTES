#!/bin/bash

test_name=$1

# mkdir -p /home/rinske/Github/ContainersRTES/logs/memory_logs

# Log directories
host_log_dir="/home/rinske/Github/ContainersRTES/logs/memory_logs/experiments"  # Host directory for logs
container_log_dir="/app/logs"  # Container directory for logs

# Python script directories
host_memory_test_dir="/home/rinske/Github/ContainersRTES/src/experiments/m1"  # Directory containing memory_test.py
host_memory_calculations_dir="/home/rinske/Github/ContainersRTES/src/memory_calculations"  # Directory containing memory calculation scripts

for i in {0..9}; do
    # Run the Docker container with volume mappings for logs and scripts
    sudo docker run --rm \
        -v "$host_log_dir:$container_log_dir" \
        -v "$host_memory_test_dir:/app/experiments/m1" \
        -v "$host_memory_calculations_dir:/app/memory_calculations" \
        general_container:1.0 /app/experiments/m1/memory_test.py $test_name $i experiment

    echo "Finishing experiment $i"
done