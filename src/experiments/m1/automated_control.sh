#!/bin/bash

test_name=$1


for i in {0..9}; do
    # Change to experiment name directory
    python memory_test.py $test_name $i control

    echo "Finishing experiment"

done

