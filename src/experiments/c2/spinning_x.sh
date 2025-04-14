#!/bin/bash


for i in {0..10}; do
    # Change to experiment name directory
    sudo docker run -v /home/rinske/Github/ContainersRTES/logs/cpu_logs/e2/"...":/host_log_files cpu_container:1.0

    echo "Created new container"

done

