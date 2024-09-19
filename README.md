# STEMNET-Daily-Files
The purpose of this repository is to create a data infrastructure that will communicate with the STEMNET server at the University of Alabama Huntsville. In particular, the goal is to give anyone the capability to create clean daily files from all available stations on the server on their own machines.

# What is a daily file? 
A daily file contains soil moisture observations in a standard format, where observations at particular sites are listed for a particular observation date. For example, here is the first 21 hours of a 24 hour daily file for 9-18-24 at the grant station.
```
id: SN003004
name: Grant
location: -86.1601, 34.564751
depths: 20;12;8;2
09-2024-18

Date, m0, m1, m2, m3, m4, t0, t1, t2, t3, t4, vpv, vb, vc
2024-09-18 00:00:00+00:00, 17.270, 18.043, 18.509, 21.112, -999.99, 22.000, 22.062, 22.312, 22.812, -999.99, 367.250, 1924.00, 3164.00
2024-09-18 01:00:00+00:00, 17.266, 18.043, 18.517, 21.089, -999.99, 22.000, 22.125, 22.375, 22.562, -999.99, 33.0000, 1921.62, 3164.00
2024-09-18 02:00:00+00:00, 17.275, 18.047, 18.509, 21.066, -999.99, 22.062, 22.187, 22.375, 22.375, -999.99, 34.0000, 1919.75, 3164.12
2024-09-18 03:00:00+00:00, 17.270, 18.047, 18.513, 21.047, -999.99, 22.062, 22.187, 22.312, 22.125, -999.99, 34.2500, 1918.12, 3164.25
2024-09-18 04:00:00+00:00, 17.270, 18.051, 18.513, 21.024, -999.99, 22.062, 22.187, 22.250, 21.875, -999.99, 37.6250, 1917.00, 3164.50
2024-09-18 05:00:00+00:00, 17.270, 18.047, 18.509, 21.001, -999.99, 22.062, 22.187, 22.250, 21.500, -999.99, 39.6250, 1915.87, 3164.50
2024-09-18 06:00:00+00:00, 17.279, 18.043, 18.505, 20.982, -999.99, 22.062, 22.125, 22.125, 21.187, -999.99, 40.2500, 1914.87, 3164.62
2024-09-18 07:00:00+00:00, 17.270, 18.051, 18.497, 20.962, -999.99, 22.062, 22.125, 22.000, 20.937, -999.99, 40.1250, 1913.75, 3164.62
2024-09-18 08:00:00+00:00, 17.283, 18.043, 18.497, 20.943, -999.99, 22.062, 22.062, 21.875, 20.625, -999.99, 39.8750, 1912.75, 3164.75
2024-09-18 09:00:00+00:00, 17.283, 18.047, 18.501, 20.920, -999.99, 22.062, 22.000, 21.750, 20.375, -999.99, 39.1250, 1911.75, 3164.75
2024-09-18 10:00:00+00:00, 17.287, 18.043, 18.493, 20.905, -999.99, 22.062, 21.937, 21.625, 20.187, -999.99, 37.8750, 1910.62, 3164.75
2024-09-18 11:00:00+00:00, 17.279, 18.047, 18.489, 20.882, -999.99, 22.062, 21.812, 21.500, 20.000, -999.99, 45.7500, 1909.37, 3164.87
2024-09-18 12:00:00+00:00, 17.287, 18.043, 18.485, 20.867, -999.99, 22.000, 21.750, 21.375, 19.812, -999.99, 2256.00, 1908.12, 3164.75
2024-09-18 13:00:00+00:00, 17.303, 18.055, 18.493, 20.867, -999.99, 22.000, 21.687, 21.250, 19.812, -999.99, 2565.12, 1907.25, 3164.00
2024-09-18 14:00:00+00:00, 17.316, 18.060, 18.501, 20.870, -999.99, 21.937, 21.562, 21.125, 20.250, -999.99, 2041.50, 1917.62, 3163.37
2024-09-18 15:00:00+00:00, 17.295, 18.071, 18.513, 20.832, -999.99, 21.937, 21.500, 21.062, 21.000, -999.99, 2048.37, 1930.75, 3163.25
2024-09-18 16:00:00+00:00, 17.287, 18.060, 18.505, 20.794, -999.99, 21.875, 21.437, 21.125, 21.562, -999.99, 2041.87, 1926.50, 3163.37
2024-09-18 17:00:00+00:00, 17.254, 18.071, 18.513, 20.732, -999.99, 21.812, 21.437, 21.250, 22.250, -999.99, 2055.12, 1945.50, 3163.12
2024-09-18 18:00:00+00:00, 17.241, 18.060, 18.505, 20.683, -999.99, 21.812, 21.500, 21.375, 22.687, -999.99, 2040.00, 1934.25, 3163.37
2024-09-18 19:00:00+00:00, 17.229, 18.068, 18.513, 20.621, -999.99, 21.812, 21.500, 21.625, 23.000, -999.99, 2038.37, 1939.75, 3163.50
2024-09-18 20:00:00+00:00, 17.225, 18.068, 18.517, 20.571, -999.99, 21.812, 21.625, 21.750, 23.250, -999.99, 2042.50, 1953.12, 3163.37
2024-09-18 21:00:00+00:00, 17.208, 18.063, 18.513, 20.514, -999.99, 21.750, 21.687, 21.937, 23.687, -999.99, 2038.62, 1959.37, 3163.25
```

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
The data can be pulled from [data.al.climate.com](https://data.alclimate.com/) and processed into daily files by running the following command in the directory containing the python software. 
```
python main.py 
```

# Crontab
To set up a crontab so that new daily file observations can be added every 10 minutes, run the following commands: 
```
crontab -e
```
Place the following command in your crontab file, where <path-to-STEMNET-Daily-files> is the location of the python software:
```
*/10 * * * * (cd <path-to-STEMNET-Daily-files> && python main.py) >/dev/null 2>&1
```

# Project Dependencies
This project is built with the Python 3.9.2 standard libraries. No special dependencies are needed. Just install python 3.9.2. You will also need wget 1.21 and curl 7.74 to run the shell scripts correctly. 
