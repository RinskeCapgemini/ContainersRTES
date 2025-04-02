#!/bin/bash

LOGDIR="./log_files"
CONTAINER_ID=$(hostname)

touch "$LOGFILE" 

LOGFILE="$LOGDIR/$CONTAINER_ID.txt"

echo "Started: " >> $(date +%s%N) >> $LOGFILE                   # >> for appending

python3 medium_calculation.py

echo "Finished: " >> $(date +%s%N) >> $LOGFILE

