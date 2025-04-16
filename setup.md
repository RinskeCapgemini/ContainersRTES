# Raspberry Pi Zero 2 W setup 

This guide can be used to setup the Raspberry Pi Zero 2 W to run the experiments on the Pi.

OS Version: For this project Raspberry Pi OS Lite (64-bit) was used. 

## Connecting to wifi
Using the sudo raspi-config command Wifi Connection can be configured. 

System Options > Wireless Lan > Enter SSID > Enter password

## Raspberry Pi Connect Beta

After installing the Raspberry Pi image was setup using the Raspberry Pi Connect Beta Services. The installation guide can be found here:
https://www.raspberrypi.com/documentation/services/connect.html 

To enable Raspberry Pi Connect the following command needs to be run every time on startup. rpi-connect on.




## Isolate CPU cores
To be able to use two isolated cores for the experiment a couple of changes to the cmdline.txt file need to be made.

Backup: sudo cp /boot/firmware/cmdline.txt /boot/firmware/cmdline.txt.bak

Command: sudo nano /boot/firmware/cmdline.txt

The following parameters need to be added to the file (on the same line). By doing this core 2 and 3 are isolated and interupts are limited. Only critical kernel interupts are still posible. 

isolcpus=2,3 nohz_full=2,3 rcu_nocbs=2,3

console=serial0,115200 console=tty1 root=PARTUUID=xxxx-xx rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait isolcpus=2,3 nohz_full=2,3 rcu_nocbs=2,3


## Install Docker CLI
https://docs.docker.com/engine/install/debian/ 



