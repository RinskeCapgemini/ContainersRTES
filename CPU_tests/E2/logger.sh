#!/bin/bash

LOGDIR="./log_files"
CONTAINER_ID=$(hostname)

LOGFILE="$CONTAINER_ID.txt"

touch "$LOGFILE" 

echo "Started: " >> $(date +%s%N) >> $LOGFILE                   # >> for appending

python3 medium_calculation.py

echo "Finished: " >> $(date +%s%N) >> $LOGFILE

