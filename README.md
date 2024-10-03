# STEMNET-Daily-Files
The purpose of this repository is to create a data infrastructure that will communicate with the STEMNET server at the University of Alabama Huntsville. In particular, the goal is to give anyone the capability to create clean daily files from all available stations on their own machines. This project also allows you to build 0-99 percentile climatology files for each station. With the added Docker capability, you can now run this as a Debian Linux container on top of Windows, Mac and Linux operating systems and have the project dependencies installed for you.  

# What is a daily file? 
A daily file contains soil moisture observations in a standard format, where observations (volumetric soil moisture %, m0, m1, m2, m3, m4, temperature C, t0, t1, t2, t3, t4) are listed for particular for a 24 hour period. For example, here is a daily file for 9-18-24 at the Grant, Alabama station (SN003004).
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
2024-09-18 22:00:00+00:00, 17.204, 18.063, 18.517, 20.487, -999.99, 21.812, 21.812, 22.125, 23.562, -999.99, 2616.25, 1967.00, 3163.37
2024-09-18 23:00:00+00:00, 17.196, 18.063, 18.505, 20.456, -999.99, 21.812, 21.875, 22.312, 23.312, -999.99, 2031.75, 1954.50, 3164.00
```

The server at [data.alclimate.com/stemmnet/stations/](https://data.alclimate.com/stemmnet/stations/) contains csv files that have all observations for the sensor period of record. This software breaks down that data into daily files so that it is easier to find data on a particular date. For example, here is the directory structure of all daily files produced by station SN003021 (Thomaston) for 2023. The daily files are `.txt` files and contain YYYYMMDD naming convention. The tree below shows daily files in 2023 for October and November.  

```
2023/
├── 10
│   ├── 27
│   │   └── 20231027.txt
│   ├── 28
│   │   └── 20231028.txt
│   ├── 29
│   │   └── 20231029.txt
│   ├── 30
│   │   └── 20231030.txt
│   └── 31
│       └── 20231031.txt
└── 11
    ├── 01
    │   └── 20231101.txt
    ├── 02
    │   └── 20231102.txt
    ├── 03
    │   └── 20231103.txt
    ├── 04
    │   └── 20231104.txt
    ├── 05
    │   └── 20231105.txt
    ├── 06
    │   └── 20231106.txt
    ├── 07
    │   └── 20231107.txt
    ├── 08
    │   └── 20231108.txt
    ├── 09
    │   └── 20231109.txt
    ├── 10
    │   └── 20231110.txt
    ├── 11
    │   └── 20231111.txt
    ├── 12
    │   └── 20231112.txt
    ├── 13
    │   └── 20231113.txt
    ├── 14
    │   └── 20231114.txt
    ├── 15
    │   └── 20231115.txt
    ├── 16
    │   └── 20231116.txt
    ├── 17
    │   └── 20231117.txt
    ├── 18
    │   └── 20231118.txt
    ├── 19
    │   └── 20231119.txt
    ├── 20
    │   └── 20231120.txt
    ├── 21
    │   └── 20231121.txt
    ├── 22
    │   └── 20231122.txt
    ├── 23
    │   └── 20231123.txt
    ├── 24
    │   └── 20231124.txt
    ├── 25
    │   └── 20231125.txt
    └── 26
        └── 20231126.txt
```

# Directory Set up 
Below is a diagram of structure for this software including descriptions of each directory. 

```
# * signifies directory automatically made by project 
.
├── README.md
├── climatology_files *
├── daily_files *
├── get_data.py
├── get_metadata.sh
├── get_station.sh
├── helper_functions.py
├── logfiles *
│   └── last_station_times *
├── make_climatology.py
├── main.py
├── metadata *
├── movelog.sh
├── process_daily.py
├── reset_factory.sh
└── station_data *
```

### metadata = location of the soil moisture station metadata 
	
	Contains the soil moisture station metadata file returned
	by get_metadata.sh. 
 

### station_data = location of the csv files containing soil moisture data
	
	Contains the csv files of soil moisture data returned 
	from get_station.sh

### daily_files = location of the daily soil moisture data

    Contains subdirectories of each station. Inside of the station directory 
    will be year. Inside of each year will be a julian day directory. Inside of 
    the julian day directory will be a textfile with the measured soil moisture data. 
### climatology_files = location of the 0-99 percentile files for each station

    Contains the <station>.txt climatology file with 0-99 percentile values 
    for each feature in all of the daily files.


To create `climatology_files`, make sure you have some daily files in `/daily_files/` and run:

```
python make_climatology.py
```
### log_files = the location of files pertaining to error logs for a particular run

    Contains DATE_error.log file where DATE is the timestamp of the system run 
    time and the error.log file contains system warnings and errors. 
    last_station_times = location of the last measurement text file
    
### last_station_times

    Contains the last_known_measurement.txt file that can be compared
    with any new data that is recieved by this system to write 
    out information to the correct daily file. The last_known_measurement.txt
    file contains the last known data that was recieved by this system.

# Python Scripts

### main.py 
    a script to drive the entire data infrustructure process. 

### helper_functions.py 
    a module that contains helper functions that can be imported into other scripts. 
    
### getdata.py 
    a script to retrieve the up to date metadata file from the Alabama stemnet server. 
	
### process_daily.py
    a script to process the daily files for each station csv file that is pulled from the Alabama stemnet server.

### read_routine.py
    contains the ReadRoutine class that can be used to read dailyfiles into a programable object. 

### make_climatology.py 
    calculates 0-99 percentile values into standard climatology files for each station.  

# Shell Scripts 

### get_station.sh 
    shell script used by getdata.py to pull a station from data.alclimate.com
	
### get_metadata.sh 
    script used by getdata.py to pull metadata from data.alclimate.com
	
### movelog.sh 
    script to move the logfile generated by process_daily.py from the scripts dir to the logfiles dir and generate an appropriate file name. 

# How To Run
The data can be pulled from [data.al.climate.com](https://data.alclimate.com/) and processed into daily files by running the following command in the directory containing the python software. 
```
python main.py 
```
This will create all daily files from the oldest to most recent observation times in the `daily_files` directory. If `main.py` is called again, it will not reprocess the oldest timestamps. It will only process observations that it has not seen. If you would like to check what the last observation time processed was for each station, go to the `logfiles/last_station_times/` directory and the most recent timestamp is stored in a `<station>.csv` file that is utilized by the software for each `main.py` call afterwards.

# Crontab Setup 
The data at[data.al.climate.com](https://data.alclimate.com/) is updated every hour. Therefore, to automate python being called every hour so that data files can be updated, set up a chrontab and call `main.py`. For example, to setup a crontab so that new daily file observations can be added to daily files in the `daily_files` directory every hour, (even when you are away from your machine and it is sleeping) run the following commands: 

### set up a new crontab
```
crontab -e
```
### add a cron job 
Place the following command in your crontab file, where `<path-to-STEMNET-Daily-files>` is the location of the python software:
```
*/60 * * * * (cd <path-to-STEMNET-Daily-files> && python main.py) >/dev/null 2>&1
```

# Project Dependencies
This project is built with the Python standard libraries. No special Python dependencies are needed from package managers. You will also need `wget` and `curl` to run the shell scripts correctly. 
The tested working versions are Python 3.9.2, wget 1.21 and curl 7.74 on a Raspberry Pi 4. 

# Optional Docker Container setup 
The wonderful [@wbcraft](@wbcraft) set up a docker file and a docker compose file to run this project and all of its dependencies inside of a docker container. This means that you can build the container on your your machine using the docker file. Or, you can pull the image from Docker Hub and run the container on your machine. To pull the image from Docker Hub and start running it, move inside the `STEMNET-Daily-Files` directory and run the following command:

```
#builds the container 
docker compose up -d 
```

```
#step inside the container 
docker exec -it stemnet bash #you will be root and should see all of the STEMNET python and shell script files 
```

This container will give you a Raspbery Pi OS on top of your Windows, Mac or Linux Operating system and the cron job will automatically be deployed. Come back at the 5th minute of every hour and new files should appear in `daily_files` that were processed by the software. The `daily_files` will be written inside of `/root/stemnet/STEMNET-Daily-Files/` directory and shared on a referenced volume on the host machnine. To see where the data is being written on your machine from the container, run the following command:

```
#look at available volumes
docker volume ls
```

```
#inspect the stemnet volume created by the docker compose file
docker volume inspect stemnet-daily-files_dailyfiles
```
You can build the docker image directly on your machine without pulling from the Docker Hub. To do that, step inside the `STEMNET-Daily-Files` directory and run the following commands:

```
docker build -t stemnet . # "." looks for the Dockerfile in STEMNET-Daily-Files.
```

Once the image builds, you will be able to see the built image on your machine by running the following command:

```
docker image ls
```

You can then start a container from the built image by running

```
docker start <image> #where image is the IMAGE ID or the REPOSITORY found after running docker image ls
```
