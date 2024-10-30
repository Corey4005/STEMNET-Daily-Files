# STEMNET-Daily-Files
The purpose of this repository is to create a data infrastructure that will communicate with the STEMNET server at the University of Alabama Huntsville. In particular, the goal is to give anyone the capability to create clean daily files from all available stations on their own machines. This project also allows you to build 0-99 percentile climatology files for each station. With the Docker capability, you can run this as a Linux container on top of another Linux or Mac operating system and have the project dependencies installed for you. The container also automates the cron job setup so that daily file calls are made by the software on the 5th minute of every hour and climatology calls are made every Wednesday at 12:15. The output files are then dumped on your host machine in a convenient volume directory. 

# What is a daily file? 
A daily file contains soil moisture observations in a standard format, where observations are listed for particular 24 hour period. Moisture values (m0, m1, m2, m3 and m4) are associated with depths beginning with the smallest number first, and are in volumetric soil moisutre (cm<sup>3</sup>/cm<sup>3</sup>) units. If the depth does not exist for a particular file, the column will be replaced with `-999.99`. Temperature values are also associated with the same depths as their mositure counterpart (t0 is associated with m0) and are in units of celcius (C). There are also voltage readings in the file for the solar panel (vpv), the battery (vb) and the clock (vc). Here is a daily file for 9-18-24 at the Grant, Alabama station (SN003004).
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
# What is a climatology file? 

A climatology file contains the 0-99 percentile values for a particular station and is calculated over the known daily files. For example, below is a climatology file for Grant, Alabama from August of 2023 to October 2024. Using the daily file above, we can see that the 2024-09-18 23:00:00+00:00 observation for the 2 inch sensor (m0) was 17.196. According to the known climatology, this would mean that the value was between the lowest 0 and 1 percentiles for the described period. 

```
id: SN003004
name:  Grant
location: -86.1601, 34.564751
depths: 20;12;8;2
dates: 2023-08-01 19:20:00+00:00, 2024-10-04 22:00:00+00:00

percentile, m0, m1, m2, m3, m4, t0, t1, t2, t3, t4, vpv, vb, vc
0, 16.633, 17.825, 18.116, 18.956, -999.99, 4.9375, 3.375, 2.375, 0.5, -999.99, 32.125, 1645.25, 822.625
1, 19.29, 19.967, 20.729, 21.135, -999.99, 5.5625, 4.0625, 3.0, 1.125, -999.99, 33.25, 1748.5, 2955.0
2, 19.318, 20.009, 20.752, 21.184, -999.99, 6.0, 4.625, 3.8125, 2.4375, -999.99, 33.5, 1803.75, 2966.75
3, 19.345, 20.036, 20.778, 21.234, -999.99, 7.375, 6.4375, 6.0625, 4.625, -999.99, 33.5, 1824.87, 2973.37
4, 19.372, 20.083, 20.863, 21.261, -999.99, 8.3125, 7.3125, 6.625, 5.0625, -999.99, 33.625, 1846.62, 2975.12
5, 19.388, 20.121, 20.982, 21.288, -999.99, 8.625, 7.625, 6.9375, 5.5625, -999.99, 33.75, 1860.37, 3006.75
6, 19.435, 20.187, 21.066, 21.326, -999.99, 8.75, 7.75, 7.125, 5.875, -999.99, 33.875, 1870.12, 3025.12
7, 19.52, 20.268, 21.15, 21.368, -999.99, 8.8125, 7.9375, 7.375, 6.1875, -999.99, 34.0, 1876.5, 3036.87
8, 19.633, 20.399, 21.268, 21.471, -999.99, 8.9375, 8.125, 7.5625, 6.5, -999.99, 34.125, 1882.87, 3041.75
9, 19.703, 20.533, 21.506, 21.701, -999.99, 9.0, 8.25, 7.75, 6.75, -999.99, 34.125, 1888.62, 3046.87
10, 19.851, 20.721, 21.793, 21.846, -999.99, 9.125, 8.375, 7.9375, 7.0, -999.99, 34.25, 1893.5, 3050.25
11, 20.009, 20.928, 22.053, 21.904, -999.99, 9.3125, 8.5, 8.0625, 7.1875, -999.99, 34.375, 1896.75, 3054.5
12, 20.175, 21.146, 22.333, 21.984, -999.99, 9.375, 8.625, 8.1875, 7.4375, -999.99, 34.375, 1899.25, 3058.12
13, 20.279, 21.272, 22.448, 22.099, -999.99, 9.5, 8.8125, 8.3125, 7.5625, -999.99, 34.5, 1901.62, 3061.87
14, 20.322, 21.288, 22.46, 22.26, -999.99, 9.5625, 8.9375, 8.5, 7.75, -999.99, 34.625, 1904.0, 3062.62
15, 20.364, 21.295, 22.468, 22.31, -999.99, 9.6875, 9.125, 8.6875, 7.875, -999.99, 34.625, 1906.37, 3064.87
16, 20.379, 21.311, 22.479, 22.379, -999.99, 9.875, 9.3125, 9.0, 8.0625, -999.99, 34.75, 1908.5, 3067.37
17, 20.491, 21.368, 22.491, 22.433, -999.99, 10.062, 9.5625, 9.125, 8.3125, -999.99, 34.875, 1909.87, 3068.75
18, 20.571, 21.414, 22.514, 22.525, -999.99, 10.25, 9.75, 9.25, 8.5, -999.99, 34.875, 1911.0, 3071.25
19, 20.721, 21.689, 22.876, 22.575, -999.99, 10.437, 9.875, 9.375, 8.6875, -999.99, 35.0, 1912.0, 3073.12
20, 20.951, 22.007, 23.264, 22.629, -999.99, 10.625, 10.0, 9.625, 8.875, -999.99, 35.125, 1912.75, 3075.0
21, 21.158, 22.318, 23.595, 22.691, -999.99, 10.75, 10.062, 9.8125, 9.0625, -999.99, 35.125, 1913.37, 3076.5
22, 21.441, 22.579, 23.956, 22.756, -999.99, 10.875, 10.25, 9.9375, 9.3125, -999.99, 35.375, 1913.87, 3078.37
23, 21.655, 22.887, 24.174, 22.822, -999.99, 11.0, 10.375, 10.062, 9.5625, -999.99, 35.375, 1914.37, 3080.62
24, 21.793, 23.023, 24.329, 22.891, -999.99, 11.125, 10.5, 10.187, 9.8125, -999.99, 35.5, 1914.75, 3083.12
25, 21.934, 23.182, 24.493, 22.992, -999.99, 11.312, 10.75, 10.312, 10.0, -999.99, 35.625, 1915.12, 3084.12
26, 22.034, 23.334, 24.528, 23.081, -999.99, 11.625, 10.937, 10.5, 10.25, -999.99, 35.75, 1915.5, 3085.37
27, 22.091, 23.446, 24.552, 23.275, -999.99, 11.812, 11.125, 10.75, 10.437, -999.99, 35.875, 1915.75, 3086.75
28, 22.133, 23.517, 24.605, 23.611, -999.99, 11.875, 11.375, 11.062, 10.687, -999.99, 36.0, 1916.0, 3088.0
29, 22.202, 23.556, 24.653, 23.992, -999.99, 12.0, 11.5, 11.25, 10.875, -999.99, 36.0, 1916.37, 3089.0
30, 22.271, 23.587, 24.717, 24.333, -999.99, 12.125, 11.812, 11.5, 11.062, -999.99, 36.125, 1916.62, 3090.25
31, 22.314, 23.665, 24.769, 24.617, -999.99, 12.375, 12.0, 11.75, 11.25, -999.99, 36.25, 1917.0, 3090.87
32, 22.341, 23.72, 24.802, 25.2, -999.99, 12.437, 12.187, 12.062, 11.437, -999.99, 36.375, 1917.37, 3091.75
33, 22.402, 23.799, 24.862, 25.711, -999.99, 12.75, 12.437, 12.25, 11.625, -999.99, 36.5, 1917.75, 3092.87
34, 22.487, 23.87, 24.952, 26.29, -999.99, 12.875, 12.562, 12.375, 11.812, -999.99, 36.625, 1918.12, 3094.0
35, 22.583, 23.984, 25.082, 26.555, -999.99, 12.937, 12.812, 12.562, 12.062, -999.99, 36.75, 1918.5, 3094.5
36, 22.729, 24.008, 25.196, 26.857, -999.99, 13.0, 12.937, 12.687, 12.312, -999.99, 36.875, 1918.87, 3095.62
37, 22.887, 24.126, 25.249, 27.15, -999.99, 13.062, 13.062, 12.812, 12.5, -999.99, 37.0, 1919.37, 3096.5
38, 23.159, 24.325, 25.327, 27.424, -999.99, 13.187, 13.125, 12.937, 12.687, -999.99, 37.125, 1919.75, 3097.87
39, 23.412, 24.525, 25.479, 27.625, -999.99, 13.375, 13.25, 13.125, 12.875, -999.99, 37.375, 1920.25, 3098.5
40, 23.673, 24.737, 25.698, 28.028, -999.99, 13.562, 13.375, 13.25, 13.125, -999.99, 37.5, 1920.62, 3099.25
41, 23.945, 24.907, 25.836, 28.271, -999.99, 13.687, 13.5, 13.375, 13.312, -999.99, 37.75, 1921.12, 3100.5
42, 24.095, 25.098, 25.915, 28.354, -999.99, 13.812, 13.687, 13.562, 13.5, -999.99, 37.875, 1921.62, 3101.37
43, 24.265, 25.281, 26.033, 28.433, -999.99, 14.125, 13.937, 13.75, 13.75, -999.99, 38.25, 1922.12, 3107.12
44, 24.709, 25.47, 26.142, 28.54, -999.99, 14.375, 14.125, 14.0, 13.937, -999.99, 38.625, 1922.75, 3133.75
45, 25.057, 25.578, 26.316, 28.709, -999.99, 14.5, 14.437, 14.312, 14.125, -999.99, 39.125, 1923.25, 3151.75
46, 25.438, 25.765, 26.397, 28.87, -999.99, 14.937, 14.625, 14.437, 14.312, -999.99, 40.125, 1924.0, 3162.37
47, 27.119, 26.218, 26.491, 29.041, -999.99, 15.375, 14.812, 14.625, 14.562, -999.99, 45.0, 1924.62, 3282.0
48, 27.607, 26.628, 26.603, 29.127, -999.99, 15.687, 15.187, 14.875, 14.75, -999.99, 82.0, 1925.37, 3283.62
49, 28.903, 26.745, 26.753, 29.223, -999.99, 15.875, 15.375, 15.062, 14.937, -999.99, 266.5, 1926.12, 3284.37
50, 29.998, 26.892, 26.862, 29.325, -999.99, 16.0, 15.5, 15.25, 15.125, -999.99, 720.125, 1926.87, 3285.37
51, 30.452, 27.106, 26.927, 29.432, -999.99, 16.125, 15.625, 15.437, 15.312, -999.99, 1282.75, 1927.75, 3286.5
52, 31.114, 27.291, 26.988, 29.573, -999.99, 16.312, 15.937, 15.687, 15.5, -999.99, 1703.5, 1928.62, 3287.37
53, 31.587, 27.398, 27.058, 29.681, -999.99, 16.437, 16.187, 15.937, 15.687, -999.99, 1960.87, 1929.25, 3288.25
54, 31.776, 27.558, 27.181, 29.834, -999.99, 16.625, 16.375, 16.187, 15.875, -999.99, 2030.75, 1930.12, 3288.62
55, 31.83, 27.832, 27.362, 30.038, -999.99, 16.812, 16.625, 16.437, 16.125, -999.99, 2031.37, 1930.87, 3289.0
56, 31.857, 28.092, 27.625, 30.284, -999.99, 17.187, 16.937, 16.687, 16.375, -999.99, 2031.87, 1931.62, 3289.87
57, 31.933, 28.262, 28.161, 30.652, -999.99, 17.562, 17.187, 16.812, 16.687, -999.99, 2032.25, 1932.37, 3290.75
58, 32.087, 28.419, 28.313, 31.041, -999.99, 17.75, 17.375, 17.062, 17.062, -999.99, 2032.62, 1933.12, 3291.37
59, 32.153, 28.512, 28.406, 31.156, -999.99, 17.875, 17.562, 17.375, 17.375, -999.99, 2033.12, 1934.0, 3292.12
60, 32.23, 28.648, 28.447, 31.336, -999.99, 18.0, 17.875, 17.812, 17.625, -999.99, 2033.5, 1934.87, 3292.87
61, 32.269, 28.822, 28.555, 31.533, -999.99, 18.25, 18.187, 18.187, 17.937, -999.99, 2034.0, 1935.75, 3294.37
62, 32.302, 29.132, 28.615, 31.641, -999.99, 18.5, 18.562, 18.437, 18.187, -999.99, 2034.5, 1936.87, 3295.25
63, 32.357, 29.257, 28.756, 31.716, -999.99, 18.75, 18.812, 18.75, 18.562, -999.99, 2034.87, 1937.62, 3296.12
64, 32.497, 29.393, 28.856, 31.841, -999.99, 19.062, 19.062, 18.937, 18.875, -999.99, 2035.5, 1938.62, 3297.0
65, 32.542, 29.676, 28.908, 31.928, -999.99, 19.437, 19.25, 19.125, 19.187, -999.99, 2036.12, 1939.75, 3297.62
66, 32.576, 29.814, 28.946, 31.971, -999.99, 19.625, 19.375, 19.375, 19.5, -999.99, 2036.75, 1941.0, 3298.37
67, 32.609, 29.888, 29.017, 32.004, -999.99, 19.687, 19.625, 19.625, 19.75, -999.99, 2037.5, 1942.25, 3299.0
68, 32.666, 30.043, 29.079, 32.037, -999.99, 19.812, 20.062, 20.062, 20.0, -999.99, 2038.25, 1943.5, 3299.62
69, 32.716, 30.118, 29.175, 32.065, -999.99, 19.937, 20.312, 20.437, 20.25, -999.99, 2039.0, 1944.75, 3300.12
70, 32.767, 30.163, 29.291, 32.092, -999.99, 20.125, 20.5, 20.687, 20.5, -999.99, 2039.87, 1946.12, 3300.62
71, 32.824, 30.284, 29.461, 32.125, -999.99, 20.312, 20.812, 21.0, 20.687, -999.99, 2041.12, 1947.62, 3301.37
72, 32.858, 30.508, 29.671, 32.164, -999.99, 20.5, 21.062, 21.187, 20.937, -999.99, 2042.5, 1949.12, 3302.0
73, 33.15, 30.544, 29.706, 32.208, -999.99, 20.75, 21.312, 21.375, 21.187, -999.99, 2044.37, 1950.62, 3302.75
74, 33.185, 30.559, 29.735, 32.252, -999.99, 21.062, 21.562, 21.5, 21.437, -999.99, 2046.62, 1952.12, 3303.25
75, 33.243, 30.574, 29.799, 32.285, -999.99, 21.75, 21.687, 21.625, 21.687, -999.99, 2049.5, 1953.37, 3303.87
76, 33.446, 30.59, 29.884, 32.319, -999.99, 21.875, 21.812, 21.812, 21.937, -999.99, 2053.37, 1954.75, 3304.5
77, 33.475, 30.6, 29.928, 32.369, -999.99, 22.0, 21.937, 21.937, 22.25, -999.99, 2068.75, 1956.0, 3305.0
78, 33.487, 30.611, 30.098, 32.486, -999.99, 22.125, 22.062, 22.062, 22.5, -999.99, 2117.25, 1957.25, 3305.62
79, 33.505, 30.615, 30.214, 32.536, -999.99, 22.187, 22.187, 22.25, 22.75, -999.99, 2237.25, 1958.5, 3306.0
80, 33.522, 30.631, 30.523, 32.643, -999.99, 22.25, 22.312, 22.437, 23.0, -999.99, 2360.5, 1959.75, 3306.37
81, 33.545, 30.641, 30.765, 32.728, -999.99, 22.375, 22.437, 22.562, 23.25, -999.99, 2449.12, 1961.12, 3306.87
82, 33.581, 30.657, 30.822, 32.79, -999.99, 22.562, 22.75, 22.812, 23.5, -999.99, 2505.5, 1962.37, 3307.5
83, 33.604, 30.672, 30.848, 32.852, -999.99, 23.25, 23.312, 23.25, 23.687, -999.99, 2552.12, 1963.62, 3308.0
84, 33.622, 30.683, 30.879, 32.921, -999.99, 23.875, 23.812, 23.75, 23.937, -999.99, 2601.0, 1965.0, 3308.5
85, 33.669, 30.693, 30.905, 32.984, -999.99, 24.25, 24.375, 24.25, 24.187, -999.99, 2647.25, 1966.0, 3309.12
86, 33.71, 30.698, 30.957, 33.03, -999.99, 24.5, 24.625, 24.5, 24.375, -999.99, 2685.37, 1967.0, 3309.75
87, 33.746, 30.713, 30.994, 33.145, -999.99, 24.562, 24.812, 24.75, 24.625, -999.99, 2714.25, 1967.62, 3310.37
88, 33.764, 30.729, 31.025, 33.295, -999.99, 24.687, 24.937, 25.0, 24.875, -999.99, 2735.5, 1968.12, 3310.75
89, 33.788, 30.76, 31.067, 33.347, -999.99, 24.812, 25.125, 25.187, 25.125, -999.99, 2751.25, 1968.5, 3311.12
90, 33.799, 30.926, 31.099, 33.528, -999.99, 24.875, 25.25, 25.312, 25.375, -999.99, 2767.12, 1968.75, 3311.5
91, 33.823, 30.999, 31.13, 33.74, -999.99, 24.937, 25.375, 25.5, 25.687, -999.99, 2780.37, 1969.12, 3312.0
92, 33.864, 31.078, 31.146, 33.918, -999.99, 25.0, 25.5, 25.687, 25.937, -999.99, 2794.75, 1969.5, 3312.37
93, 33.918, 31.125, 31.156, 34.248, -999.99, 25.062, 25.562, 25.875, 26.312, -999.99, 2813.37, 1969.75, 3313.0
94, 33.966, 31.225, 31.167, 34.474, -999.99, 25.125, 25.687, 26.0, 26.625, -999.99, 2832.25, 1970.12, 3313.5
95, 34.032, 31.267, 31.183, 34.516, -999.99, 25.25, 25.875, 26.187, 27.062, -999.99, 2849.75, 1970.62, 3314.12
96, 34.086, 31.331, 31.209, 34.553, -999.99, 25.375, 26.062, 26.437, 27.562, -999.99, 2869.75, 1971.12, 3314.75
97, 34.176, 31.857, 31.32, 34.584, -999.99, 25.562, 26.25, 26.687, 28.125, -999.99, 2892.25, 1971.75, 3315.62
98, 34.255, 32.065, 31.48, 34.645, -999.99, 25.75, 26.562, 27.0, 28.75, -999.99, 2916.5, 1972.25, 3316.5
99, 34.596, 32.246, 31.857, 34.7, -999.99, 26.062, 26.875, 27.437, 29.75, -999.99, 2957.62, 1972.75, 3317.5
```
# Automated Checks
This software cleans the data for you and logs all of the automated checks. 
Low and high voltage - Any voltage reading used in the Volumetric Water Content (VWC) equation that is below 950 or above 2000 for m0, m1, m2, m3, and m4 are replaced with -999.99
Bad Clock Values - On occasion, the computer will report a faulty clock time. Any clock time that is above the possible UTC+12 currently on Earth is ignored and not written out to daily files. 
Bad Time Length Values - In the early days, clock times would sometimes return timestamps that were less than the correct number of characters. These observations are ignored and not written out to daily files.
Timestamps containing characters - Sometimes, faulty values such as characters will be reported in the time stamps. Any timestamp that contains non-numeric characters will be ignored.

# VWC Equation
The equation for calculating VWC is displayed below, where mm is the voltage returned from the soil moisture sensor:

VWC = 100.0 * ((4.82E-10 * mm<sup>3</sup>) - (2.28E-6 * mm<sup>2</sup>) + (3.898E-3 * mm) - 2.154) 

# Docker Container setup 
First install docker:
- [Linux install](https://docs.docker.com/engine/install/)
- [Mac install](https://docs.docker.com/engine/install/)
  
The wonderful [@wbcraft](https://github.com/wbcraft) helped set up the first Docker files and their associated Docker Compose file to run this project and all of its dependencies inside of a container. This means you can pull the image from Docker Hub and run the container on your machine. To pull the image from Docker Hub and start running it, move inside the [`STEMNET-Daily-Files/debian-linux-docker-compose`](https://github.com/Corey4005/STEMNET-Daily-Files/tree/main/debian-linux-docker-compose-file) directory and follow the associated instructions. 

To build the containers yourself, move inside the [`STEMNET-Daily-Files/debian-linux-build`](https://github.com/Corey4005/STEMNET-Daily-Files/tree/main/debian-linux-build) directory and follow the assocated instructions. 

The [`stemnet-daily-files`](https://hub.docker.com/repository/docker/corey4005/stemnet-daily-files/general) image is located on the Docker hub and is available to be pulled to a host machine. 
