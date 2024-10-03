#!/bin/bash

dailypath=./daily_files
logpath=./logfiles

#set the owner
owner=$(stat -c "%u" $dailypath)
group=$(stat -c "%g" $dailypath)

#chanign the owner and group programatically inside the container 
sudo chown -R $owner $dailypath
sudo chgrp -R $group $dailypath
sudo chown -R $owner $logpath
sudo chgrp -R $group $logpath

echo "$dailypath set to $owner:$group"
echo "$logpath set to $owner:$group"
