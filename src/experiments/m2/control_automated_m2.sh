#!/bin/bash

# Directory on the host system where the CSV log file will be stored
HOST_LOGDIR="/home/rinske/Github/ContainersRTES/logs/memory_logs/m2/control/"  # Host directory for logs

mkdir -p "$HOST_LOGDIR"  # Create the log directory if it doesn't exist

OUTSIDE_LOGFILE="$HOST_LOGDIR/control_outside_logs.csv"

CONTAINER_LOGDIR="/app/logs"  # Container directory for logs

# Python script directories
HOST_EXPERIMENT_DIR="/home/rinske/Github/ContainersRTES/src/experiments/m2"  # Directory containing memory_test.py
HOST_MEMORY_CALCULATIONS="/home/rinske/Github/ContainersRTES/src/memory_calculations"  # Directory containing memory calculation scripts

test_name=$1

# Create the CSV log file with a header if it does not already exist
if [ ! -f "$OUTSIDE_LOGFILE" ]; then
    echo "Container ID, Experiment (i), Start Time (ns),Finish Time (ns),Duration (ns)" > $OUTSIDE_LOGFILE
fi

for test in {0..9}; do
    for measurement in $(seq 0 $test); do
        # Log the start time of the container execution
        START_TIME=$(date +%s%N)

        # Run the Docker container, wait for finish before moving on, with mounted files.
        CONTAINER_ID=$(sudo docker run \
            -v "$HOST_LOGDIR:$CONTAINER_LOGDIR" \
            -v "$HOST_EXPERIMENT_DIR:/app/experiments/m2" \
            -v "$HOST_MEMORY_CALCULATIONS:/app/memory_calculations" \
            general_container:1.0 /app/experiments/m2/memory_test.py $test_name $test $measurement control)

        # Log the finish time of the container execution
        FINISH_TIME=$(date +%s%N)

        # Calculate the duration of the container execution
        DURATION=$((FINISH_TIME - START_TIME))

        # Append the log entry to the CSV file
        echo "$CONTAINER_ID,$test,$START_TIME,$FINISH_TIME,$DURATION" >> $OUTSIDE_LOGFILE

        echo "Finishing measurement $measurement"
    done

    echo "Finishing test $test"
done

