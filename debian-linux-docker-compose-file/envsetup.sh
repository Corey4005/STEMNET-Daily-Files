#!/bin/bash
# a script to automatically set the env file 
USER_ENV=$(id -u $USER)
echo "setting USER variable in env_file.env to $USER_ENV"
#clear the file 
: > ./.env
#set the USER variable 
echo "LOCAL_USER_ID=$USER_ENV" >> ./.env
