#!/bin/bash

test_name=$1

for i in {0..9}; do
    Change to experiment name directory
    sudo taskset -c 3 python3 cpu_test.py $test_name $i control

    echo "Finishing experiment"

done
