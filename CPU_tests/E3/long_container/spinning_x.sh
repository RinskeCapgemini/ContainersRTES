#!/bin/bash


for i in {0..99}; do
    # Change to container name
    sudo docker run -d --memory="100m" -v /home/pirinske/GitHub/ContainersRTES/CPU_tests/E3/long_container/log_files:/host_log_files e2:long_script

    echo "Created new container"

done

