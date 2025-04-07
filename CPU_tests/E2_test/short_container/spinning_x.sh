#!/bin/bash


for i in {0..10}; do
    # Change to container name
    sudo docker run -d -v /home/rinske/Github/ContainersRTES/CPU_tests/E2_test/short_container/log_files:/host_log_files simple_script:1.0

    echo "Created new container"

done

