#!/bin/bash 
# Add local user
# Either use the LOCAL_USER_ID if passed in at runtime or
# fallback

(cd /home/user/stemnet/ && python main.py) >> /home/user/stemnet/logfiles/main_output.log
(cd /home/user/stemnet/ && python make_climatology.py) >> /home/user/stemnet/logfiles/make_climatology_output.log

USER_ID=${LOCAL_USER_ID:-9001}

echo "Starting with UID : $USER_ID"
 
if id user; then
    echo "reasigning UID to ${USER_ID} for user"
    usermod -u $USER_ID  user
    groupmod -g $USER_ID user
else
    echo "creating user with ${USER_ID}"
    useradd --shell /bin/bash -u $USER_ID -o -c "" -m user
fi

service cron start
export HOME=/home/user
exec /usr/local/bin/gosu user bash
