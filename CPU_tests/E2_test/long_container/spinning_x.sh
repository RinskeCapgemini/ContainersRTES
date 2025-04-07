#!/bin/bash


for i in {0..10}; do
    # Change to container name
    sudo docker run -d -v /home/rinske/GitHub/ContainersRTES/CPU_tests/E2_test/long_container/log_files:/host_log_files long_script:1.0

    echo "Created new container"

done

