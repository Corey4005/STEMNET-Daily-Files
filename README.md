# STEMNET-Daily-Files
The purpose of this repository is to create a data infrastructure that will communicate with the STEMNET server at the University of Alabama Huntsville. In particular, the goal is to give anyone the capability to create clean daily files from all available stations on their own machines. This project also allows you to build 0-99 percentile climatology files for each station. With the added Docker capability, you can now run this as a Linux container on top of another Linux or Mac operating system and have the project dependencies installed for you. The container also automates the cron job setup so that calls are made by the software on the 5th minute of every hour and dumped on your host machine in a convenient volume directory. 

# What is a daily file? 
A daily file contains soil moisture observations in a standard format, where observations are listed for particular for a 24 hour period. Moisture values (m0, m1, m2, m3 and m4) are associated with depths beginning with the smallest number first, and are in volumetric soil moisutre (cm<sup>3</sup>/cm<sup>3</sup>) units. If the depth does not exist for a particular file, the column will be replaced with `-999.99`. Temperature values are also associated with the same depths as their mositure counterpart (t0 is associated with m0) and are in units of celcius (C). There are also voltage readings in the file for the solar panel (vpv), the battery (vb) and the clock (vc). Here is a daily file for 9-18-24 at the Grant, Alabama station (SN003004).
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
# Docker Container setup 
First install docker:
- [Linux install](https://docs.docker.com/engine/install/)
- [Mac install](https://docs.docker.com/engine/install/)
  
The wonderful [@wbcraft](https://github.com/wbcraft) helped set up the first Docker files and their associated Docker Compose file to run this project and all of its dependencies inside of a container. This means you can pull the image from Docker Hub and run the container on your machine. To pull the image from Docker Hub and start running it, move inside the [`STEMNET-Daily-Files/debian-linux-docker-compose`](https://github.com/Corey4005/STEMNET-Daily-Files/tree/main/debian-linux-docker-compose-file) directory and follow the associated instructions. 

To build the containers yourself, move inside the [`STEMNET-Daily-Files/debian-linux-build`](https://github.com/Corey4005/STEMNET-Daily-Files/tree/main/debian-linux-build) directory and follow the assocated instructions. 
