#!/bin/bash


for i in {0..99}; do
    # Change to container name
    sudo docker run --rm -v /home/pirinske/GitHub/ContainersRTES/CPU_tests/E2/short_container/log_files:/host_log_files e2:simple_script

    echo "Created new container"

done

