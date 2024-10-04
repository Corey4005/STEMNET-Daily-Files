#!/bin/bash
# setup for docker 
mkdir ../daily_files
mkdir ../logfiles
mkdir ../climatology_files

cd ../ && docker compose up -d 
