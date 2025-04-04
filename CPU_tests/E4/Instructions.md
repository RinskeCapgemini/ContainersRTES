# E4

This experiment is a follow-up experiment based on E3. In E3 spinning multiple containers was impossible after 2 contianers. This experiment was used to determine the bottleneck.

Cores:
1. System processes
2. Dockerd and containerd processes
3. Core to run containers
4. T.b.d

To isolate the cores the following setup was used:

1. in /boot/firmware/cmdline.txt add the following parameters (must be 1 line):

console=serial0,115200 console=tty1 root=PARTUUID=xxxx-xx rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait isolcpus=2,3 nohz_full=2,3 rcu_nocbs=2,3

Core 0 is now reserved for system processes.

2. Move dockerd and containerd processes to core 2

sudo taskset -pc 2 <PID>

3. Run script on core 3.

sudo bash --cpuset-cpus=3 spinning_x.sh


## Choices

For this experiment the long_calculation.py script was used to keep the containers running while spinning new ones. 



