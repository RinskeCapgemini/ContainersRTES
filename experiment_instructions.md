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

### Docker running instructions



### Experiment E1
1. Navigate to the `src/experiments/e1/` directory.
2. Run the `automated_cpu_test.py` script:
   ```bash
   python3 automated_cpu_test.py
   ```
3. Use the `plot.py` script to generate visualizations:
   ```bash
   python3 plot.py
   ```

```bash
sudo docker run --cpuset-cpus=3 -v /home/rinske/Github/ContainersRTES/CPU_tests/E1/log_files:/app/logs e1:1.0
```


### Experiment E2
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

### Experiment E3
1. Navigate to the `src/experiments/e3/` directory.
2. Follow the instructions in `Instructions.md` to run the experiment.

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
