#!/bin/bash

LOGDIR="./log_files"
LOGFILE="$LOGDIR/container_performance.log"

container_name="e2:simple_script"

touch "$LOGFILE" 

    if [ ! -f "$LOGFILE"]; then
        echo "timestamp,container_name,runtime_ms" > "$LOGFILE"
    fi


log() {
    echo "$1,$2,$3" >> "$LOGFILE"
}

create_container() {
    local start_time=$(date +%s%N)

    docker run --rm "$container_name" > /dev/null 2>&1

    local finished_time=$(date +%s%N)
    local elapsed_ns=$((finished_time - start_time))
    local elapsed_ms=$((elapsed_ns / 1000000))

    log "$(date '+%Y-%m-%d %H:%M:%S')" "$container_name" "$elapsed_ms"

    echo "Created new container"
    
}

while true ; do
    
    create_container &

done