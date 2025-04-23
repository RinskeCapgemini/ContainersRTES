#!/bin/bash
# Control uses same code as experiment i3. Control is reading one 1GB file

# Check if the USB is already mounted
if ! mountpoint -q /mnt/usb; then
    sudo mount -o sync /dev/sda1 /mnt/usb
fi


# Log directories
host_log_dir="/home/rinske/Github/ContainersRTES/logs/io_logs/i3/"  # Host directory for logs
container_log_dir="/app/logs"  # Container directory for logs

# Directories containing code files
host_io_test_dir="/home/rinske/Github/ContainersRTES/src/experiments/i3"  # Directory containing io_test.py

# External USB directory 
host_usb_dir="/mnt/usb"  # Host directory for external USB
container_usb_dir="/app/usb"  # Container directory for external USB

# CSV file to store experiment data container runtimes
csv_file="${host_log_dir}control/control_container_time.csv"


# Add CSV header if the file doesn't exist
if [ ! -f "$csv_file" ]; then
    echo "Experiment Name,Run Number,Start Time,Finish Time" > "$csv_file"
fi

for i in {0..9}; do
    # Log the start time
    start_time=$(date '+%Y-%m-%d %H:%M:%S.%N')  # Human-readable time with nanoseconds

    # Run the Docker container with volume mappings for logs, scripts, and USB
    sudo docker run --rm \
        -v "$host_log_dir:$container_log_dir" \
        -v "$host_io_test_dir:/app/experiments/i3" \
        -v "$host_usb_dir:$container_usb_dir" \
        general_container:1.0 /app/experiments/i3/read_control.py $i control

    # Log the finish time
    finish_time=$(date '+%Y-%m-%d %H:%M:%S.%N')  # Human-readable time with nanoseconds

    # Append the data to the CSV file
    echo "$test_name,$i,$start_time,$finish_time" >> "$csv_file"
done
