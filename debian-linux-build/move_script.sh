#!/bin/bash
#this script manages the read and write permissions of a user
USER=$(id -u user)
GROUP=$(id -g user)

#check if the mounted dir is owned by the input u:g from the environmet file 
if [[ $(stat -c "$" ./data_out) != $USER ]]; then
    chown -R $USER ./data_out
    chgrp -R $GROUP ./data_out
fi

rsync -avz /home/user/stemnet/daily_files /home/user/stemnet/transfer_station/
rsync -avz /home/user/stemnet/climatology_files /home/user/stemnet/transfer_station/
rsync -avz /home/user/stemnet/logfiles /home/user/stemnet/transfer_station/

#giving ownership to user to all new files created by root
chown -R user /home/user/stemnet/transfer_station

#giving group user to all new files created by root
chgrp -R user /home/user/stemnet/transfer_station

#moves data from particular directories owned by root to the data_out dir, owned by user
# this is the mounted location according to the docker compose file. 
rsync -avz /home/user/stemnet/transfer_station /home/user/stemnet/data_out/

#remove all of the files so that the contaainer does not have to maintain so much space.
rm -rf /home/user/stemnet/transfer_station/*
