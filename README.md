# STEMNET-Daily-Files
The purpose of this repository is to create a data infrastructure that will communicate with the STEMNET server at the University of Alabama Huntsville. In particular, the goal is to give anyone the capability to create clean daily files from all available stations on the server on their own machines.

# Directory set up 
Below is a diagram of the directory structure for this software. Please set up a `logfiles` directory and a subfolder called `last_station_times` in the same directory as the python and shell scripts. You will also need to set up a `daily_files` and `station_data` directory for the software to function properly. 

├── README.md

├── daily_files

├── get_data.py

├── get_metadata.sh

├── get_station.sh

├── helper_functions.py

├── logfiles

│   └── last_station_times

├── main.py

├── metadata

├── movelog.sh

├── process_daily.py

├── readme.txt

├── reset_factory.sh

└── station_data

# To Run
The data can be pulled from [the University of Alabama Huntsville Server](data.al.climate.com) and processed into daily files by running the following command in the directory containing the python software. 
```
python main.py 
```

# Project Dependencies
This project is built with the Python 3.9.2 standard libraries. No special dependencies are needed. Just install python 3.9.2. You will also need wget 1.21 and curl 7.74 to run the shell scripts correctly. 
