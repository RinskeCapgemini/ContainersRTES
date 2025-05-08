# Experiment Instructions

This document provides a comprehensive guide to running the experiments in this repository.

---

## Table of Contents
1. [Setup](#setup)
2. [Running Experiments](#running-experiments)
3. [Remote Connection](#remote-connection)
4. [CPU Core Isolation](#cpu-core-isolation)
5. [Docker Setup](#docker-setup)

---

## Setup

### Raspberry Pi Zero 2 W Setup
This guide assumes you are using a Raspberry Pi Zero 2 W with Raspberry Pi OS Lite (64-bit).

#### Connecting to WiFi
1. Run the following command to configure WiFi:
   ```bash
   sudo raspi-config
   ```
2. Navigate to:
   ```
   System Options > Wireless LAN > Enter SSID > Enter password
   ```

#### Enabling Raspberry Pi Connect
1. Install Raspberry Pi Connect Beta Services using the guide found [here](https://www.raspberrypi.com/documentation/services/connect.html).
2. To enable Raspberry Pi Connect, run the following command on startup:
   ```bash
   rpi-connect on
   ```
---

## Docker Setup

To install Docker CLI on the Raspberry Pi:
1. Follow the official Docker installation guide for Debian: [Docker Installation Guide](https://docs.docker.com/engine/install/debian/).
2. Use the provided `Dockerfile` in the `docker/` directory to build and run containers for the experiments.

---

## Running Experiments

### General Command
To execute CPU tests, use the following command:
```bash
taskset -c 3 python3 <test.py>
```

### Experiment running instructions



### Experiment C1
1. Update CPU-core settings in:
```bash
sudo nano /boot/firmware/cmdline.txt 
```
change file snippet to:



2. Run control experiment using the following command:

```bash
sudo taskset -3 python automated_control.sh <experiment> control
```

3. isolate docker to CPU core 2:

```bash 
sudo systemctl edit docker 
```

change file and add: 
```ini
[Service]
CPUAffinity=2
```

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl restart docker
```

4. Run the automated experiment
```bash
bash automated_experiment.sh <test name> container+engine 
```
5. isolate docker to CPU core 3:

```bash 
sudo systemctl edit docker 
```

change file and add: 
```ini
[Service]
CPUAffinity=3
```

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl restart docker
```

6. Run the automated experiment
```bash
bash automated_experiment.sh <test name> container+engine 
```


### Experiment C2
1. Navigate to the `src/experiments/e2/` directory.
2. Use the `container_spin.sh` script to spin up containers:
   ```bash
   ./container_spin.sh
   ```
3. Format log files using `logfiles_formatter.py`:
   ```bash
   python3 logfiles_formatter.py
   ```
4. Generate plots using `plots.py`:
   ```bash
   python3 plots.py
   ```

### Experiment C3
1. Navigate to the `src/experiments/e3/` directory.
2. Follow the instructions in `Instructions.md` to run the experiment.

### Experiment M1

1. Run the control experiment
```bash
sudo bash autmated_control.sh <memory_function_name>
``` 
2. Run the experiment
```bash
sudo bash autmated_experiment.sh <memory_function_name>
``` 




### Experiment M2
This experiment is used to determine the effects of disabling swap memory.

1. Run the control experiment 
2. Disable swap memory by using the following command; check using htop command. 
```bash
sudo dphys-swapfile swapoff
free -h
```
3. Run the experiment for the different test scripts. 



### Experiment M3

This experiment is used to determine the effects of the container on the system when the OOM killer is enabled in panic mode. Panic mode enables the system to reboot when the OOM killer is invoked. 

Make sure swap memory is disabled.

1. Run the control experiment
```bash
sudo bash autmated_control.sh <memory_function_name>
``` 
2. Check current OOM panic settings
```bash 
cat /proc/sys/vm/panic_on_oom
```
- 0: disabled
- 1: enabled

3. Temporarily enable panic on OOM (until reboot)
```bash
sudo sysctl -w vm.panic_on_oom=1
sudo sysctl -w kernel.panic=10
```
```bash
sudo sysctl -p 
```
4. Run the experiment
```bash
sudo bash autmated_experiment.sh <memory_function_name>
``` 

---

## Remote Connection

To connect remotely to the Raspberry Pi, use the Raspberry Pi Connect Beta service. Ensure the service is enabled by running:
```bash
rpi-connect on
```

---

## CPU Core Isolation

To isolate CPU cores for the experiments:
1. Backup the `cmdline.txt` file:
   ```bash
   sudo cp /boot/firmware/cmdline.txt /boot/firmware/cmdline.txt.bak
   ```
2. Edit the file:
   ```bash
   sudo nano /boot/firmware/cmdline.txt
   ```
3. Add the following parameters to the same line:
   ```
   isolcpus=2,3 nohz_full=2,3 rcu_nocbs=2,3
   ```
   Example:
   ```
   console=serial0,115200 console=tty1 root=PARTUUID=xxxx-xx rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait isolcpus=2,3 nohz_full=2,3 rcu_nocbs=2,3
   ```

---



## Notes
- Ensure all dependencies are installed before running the experiments.
- Refer to the individual experiment directories for additional details and scripts.
