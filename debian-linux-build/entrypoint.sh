#!/bin/bash
service cron start 
(cd /home/user/stemnet/ && python /home/user/stemnet/main.py && python /home/user/stemnet/make_climatology.py) >> ./logfiles/python_output.log

# Add local user
# Either use the LOCAL_USER_ID if passed in at runtime or
# fallback

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

export HOME=/home/user
exec /usr/local/bin/gosu user bash
