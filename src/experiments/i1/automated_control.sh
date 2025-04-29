#!/bin/bash

# Check if the USB is already mounted
if ! mountpoint -q /mnt/usb; then
    sudo mount -o sync /dev/sda1 /mnt/usb
fi

test_name=$1

# for i in {0..9}; do
# Change to experiment name directory
sudo python io_test.py $test_name 0 control

echo "Finishing experiment"

# done


sudo umount /mnt/usb