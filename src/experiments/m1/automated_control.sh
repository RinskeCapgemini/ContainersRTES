#!/bin/bash

# Run without sudo 

test_name=$1


# for i in {0..9}; do
# Change to experiment name directory
python memory_test.py $test_name 0 control

echo "Finishing experiment"

# done
