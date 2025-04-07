#!/bin/bash

LOGDIR="./log_files"
LOGFILE="$LOGDIR/container_performance.csv"

container_name="e2:mid_script"

rm "$LOGFILE"

touch "$LOGFILE" 

echo "timestamp,container_name,runtime_ms,active_containers" > "$LOGFILE"

log() {
    echo "$1,$2,$3" >> "$LOGFILE"
}

create_container() {
    local start_time=$(date +%s%N)

    sudo docker run -d "$container_name"                # -d flag -> run container in background -> script continues, but time is not accurate; container is not finished.  

    local finished_time=$(date +%s%N)                   # Resulting finished_time is not measured when the containers is actually done. 
    local elapsed_ns=$((finished_time - start_time))           
    local elapsed_ms=$((elapsed_ns / 1000000))

    running_containers=$(sudo docker ps -q --filter ancestor="$container_name")

    echo "$running_containers" 

    log "$(date '+%Y-%m-%d %H:%M:%S')" "$container_name" "$elapsed_ms" "$running_containers"

    echo "Created new container"
    
}

while true ; do
    
    create_container &
    sleep 1.0

done