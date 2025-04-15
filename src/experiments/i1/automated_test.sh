#!/bin/bash
test_name=$1

sudo mount /dev/sda1 /mnt/usb

# Directories
host_log_dir="/home/rinske/Github/ContainersRTES/logs/io_logs/"  # Host directory for logs
container_log_dir="/app/logs"  # Container directory for logs

host_io_test_dir="/home/rinske/Github/ContainersRTES/src/experiments/i1"  # Directory containing io_test.py
host_io_calculations_dir="/home/rinske/Github/ContainersRTES/src/io_calculations"  # Directory containing io calculation scripts

# External USB directory (adjust this path to your USB mount point)
host_usb_dir="/mnt/usb"  # Host directory for external USB
container_usb_dir="/app/usb"  # Container directory for external USB

for i in {0..9}; do
    # Run the Docker container with volume mappings for logs, scripts, and USB
    sudo docker run --rm \
        -v "$host_log_dir:$container_log_dir" \
        -v "$host_io_test_dir:/app/experiments/i1" \
        -v "$host_io_calculations_dir:/app/io_calculations" \
        -v "$host_usb_dir:$container_usb_dir" \
        general_container:1.0 /app/experiments/i1/io_test.py $test_name $i experiment

    echo "Finishing experiment $i"
done

