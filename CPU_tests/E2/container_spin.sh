#!/bin/bash

LOGFILE="/log_files/container_performance.log"

container_name=""

touch "$LOGFILE" 

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOGFILE"
}

create_container() {
    local start_time=$(date +%s%N)

    docker run --rm "$container_name" > /dev/null 2>&1

    local finished_time=$(date +%s%N)
    local elapsed_ns=$((finished_time_time - start_time))
    local elapsed_ms=$((elapsed_ns / 1000000))
    log "Container: $container_name, Runtime: ${elapsed_ms}ms"
    
}

while true ; do
    
    create_container &

    sleep 1

done