#!/bin/bash


sudo mount /dev/sda1 /mnt/usb

test_name=$1

for i in {0..9}; d
    # Change to experiment name directory
    sudo python io_test.py $test_name $i control

    echo "Finishing experiment"

done


sudo unmount /mnt/usb