#!/bin/bash
# a script to automatically set the env file 
USER_ENV=$(id -u $USER)
echo "setting USER variable in env_file.env to $USER_ENV"
#clear the file 
: > ./environment/env_file.env
#set the USER variable 
echo "USER=$USER_ENV" >> ./environment/env_file.env
