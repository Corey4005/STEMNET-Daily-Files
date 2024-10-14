#! /bin/bash

# This is a script to get the updated metadata from data.alclimate.com

# variables 
META='https://data.alclimate.com/stemmnet/sn_meta.txt'
OUT_DIR="$(pwd)/metadata/"
FILE_OUT="sn_meta.txt"
# wget to  put the files in the metadata dir
wget $META -O $OUT_DIR$FILE_OUT
