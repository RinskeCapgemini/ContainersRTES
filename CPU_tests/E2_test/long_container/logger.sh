#!/bin/bash

LOGDIR="/host_log_files"

mkdir -p $LOGDIR

CONTAINER_ID=$(hostname)

LOGFILE="$LOGDIR/$CONTAINER_ID.txt"

touch $LOGFILE 

echo "Started: $(date +%s%N)" >> $LOGFILE                   # >> for appending

python3 long_calculation.py

echo "Finished: $(date +%s%N)" >> $LOGFILE

