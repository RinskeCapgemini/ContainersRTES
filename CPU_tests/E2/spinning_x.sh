#!/bin/bash


for i in {0..99}; do

    sudo docker run --rm -v /home/pirinske/GitHub/ContainersRTES/CPU_tests/E2/log_files:/host_log_files e2:testing

    echo "Created new container"

done

