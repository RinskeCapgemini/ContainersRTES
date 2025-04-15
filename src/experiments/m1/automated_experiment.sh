#!/bin/bash

test_name=$1

# Log directories
host_log_dir="/home/rinske/Github/ContainerRTES/logs/experiments/m1/experiment"  # Host directory for logs
container_log_dir="/app/logs"  # Container directory for logs

# Python script directory
host_test_program_dir="/home/rinske/Github/ContainerRTES/src/memory_calculations"  # Host directory containing Python scripts

for i in {0..9}; do
    # Run the Docker container with volume mappings for logs and scripts
    sudo docker run --rm \
        -v "$host_log_dir:$container_log_dir" \
        -v "$host_test_program_dir:/app" \
        general_container:1.0 memory_test.py $test_name $i experiment

    echo "Finishing experiment $i"
done