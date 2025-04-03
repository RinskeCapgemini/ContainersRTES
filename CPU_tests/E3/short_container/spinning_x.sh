#!/bin/bash


for i in {0..10}; do
    # Change to container name
    sudo docker run -v -d /home/pirinske/GitHub/ContainersRTES/CPU_tests/E3/short_container/log_files:/host_log_files e2:simple_script

    echo "Created new container"

done

