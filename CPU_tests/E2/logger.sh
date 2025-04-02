#!/bin/bash

LOGDIR="/host_log_files"

mkdir -p $LOGDIR

CONTAINER_ID=$(hostname)

LOGFILE="$LOGDIR/$CONTAINER_ID.txt"

touch $LOGFILE 

echo "Log directory: $LOGDIR"
echo "Log file path: $LOGFILE"

echo "Started: $(date +%s%N)" >> $LOGFILE                   # >> for appending

python3 medium_calculation.py

echo "Finished: $(date +%s%N)" >> $LOGFILE

cat /host_log_files/d0d785ef40f8.txt

