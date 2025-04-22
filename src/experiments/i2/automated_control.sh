#!/bin/bash

# Check if the USB is already mounted
if ! mountpoint -q /mnt/usb; then
    sudo mount -o sync /dev/sda1 /mnt/usb
fi


for i in {0..9}; do
    # Read file from USB device Python program.
    sudo python read_io.py $i control

    echo "Finishing experiment itteration" 
done

sudo unmount /mnt/usb