#! /bin/bash

# A script to move the error log generated by process_daily.py
# into the error log directory with the appropriate file name. 

DATE=$(date +%Y%m%d%H) 
cp ./error.log ./logfiles/$DATE.log

if [ -f ./error.log ]; then
	rm ./error.log
fi
