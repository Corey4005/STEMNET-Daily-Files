#!/bin/bash
# setup for docker 
mkdir ../daily_files
mkdir ../logfiles

cd ../ && docker compose up -d 
