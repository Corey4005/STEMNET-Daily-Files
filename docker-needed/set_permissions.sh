#!/bin/bash

dailypath=./daily_files
logpath=./logfiles
climatepath=./climatology_files

#set the owner
owner=$(stat -c "%u" $dailypath)
group=$(stat -c "%g" $dailypath)

#chanign the owner and group programatically inside the container 
sudo chown -R $owner $dailypath
sudo chgrp -R $group $dailypath
sudo chown -R $owner $logpath
sudo chgrp -R $group $logpath
sudo chown -R $owner $climatepath
sudo chgrp -R $group $climatepath

echo "$dailypath set to $owner:$group"
echo "$logpath set to $owner:$group"
