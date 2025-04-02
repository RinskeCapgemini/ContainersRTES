#!/bin/bash

LOGDIR="./log_files"
LOGFILE="$LOGDIR/container_performance.csv"

container_name="e2:middle_script"

rm "$LOGFILE"

touch "$LOGFILE" 

echo "timestamp,container_name,runtime_ms,active_containers" > "$LOGFILE"

log() {
    echo "$1,$2,$3" >> "$LOGFILE"
}

create_container() {
    local start_time=$(date +%s%N)

    sudo docker run -d "$container_name" 

    local finished_time=$(date +%s%N)
    local elapsed_ns=$((finished_time - start_time))
    local elapsed_ms=$((elapsed_ns / 1000000))

    running_containers=$(sudo docker ps -q --filter ancestor="$container_name")

    echo "$running_containers" 

    log "$(date '+%Y-%m-%d %H:%M:%S')" "$container_name" "$elapsed_ms" "$running_containers"

    echo "Created new container"
    
}

while true ; do
    
    create_container &
    sleep 0.5

done