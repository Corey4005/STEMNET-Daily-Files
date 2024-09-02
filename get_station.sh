#! /bin/bash

# This is a script to get the updated soil moisture data. 
# A station is passed in via arg1 ($1) and is pulled from wget

STATION=$1
OUT_DIR="$(pwd)/station_data/"
STATION_SERVER="https://data.alclimate.com/stemmnet/stations/$STATION.csv"

wget $STATION_SERVER -O $OUT_DIR$STATION.csv 
