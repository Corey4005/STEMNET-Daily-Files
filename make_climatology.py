import os
from datetime import datetime
from read_routine import ReadRoutine
from helper_functions import update_dictionary_list
from helper_functions import calculate_percentile
cwd = os.getcwd()
stations = {} #dictionary to sort station data in 

current_time = datetime.now()
print(f'make_climatology.py call {current_time}\n')
count = 0
daily_files = os.path.join(cwd, 'daily_files')
for root, dir, files in os.walk(daily_files):
    for f in files:
        count+=1
        #dates for the file
        dates = []

        #moisture lists
        moisture_values_m0 = []
        moisture_values_m1 = []
        moisture_values_m2 = []
        moisture_values_m3 = []
        moisture_values_m4 = []

        #temperature lists
        temperature_values_t0 = []
        temperature_values_t1 = []
        temperature_values_t2 = []
        temperature_values_t3 = []
        temperature_values_t4 = []
        
        #battery lists    
        battery_values_vb = []
        battery_values_vc = []
        battery_values_vpv = []

        #reading the data from daily file
        path = os.path.join(root, f)
        rr = ReadRoutine(filepath=path).get_data()
        
        #look up the station and append the soil moisture data 
        station_id = rr.station_id

        #colllect the date information
        dates.append(rr.observation_times)
        
        #collect the soil moisture values inside of a local list
        moisture_values_m0.append(rr.m0)
        moisture_values_m1.append(rr.m1)
        moisture_values_m2.append(rr.m2)
        moisture_values_m3.append(rr.m3)
        moisture_values_m4.append(rr.m4)

        #collect the temperature information
        temperature_values_t0.append(rr.t0)
        temperature_values_t1.append(rr.t1)
        temperature_values_t2.append(rr.t2)
        temperature_values_t3.append(rr.t3)
        temperature_values_t4.append(rr.t4)
        
        #collecting battery info
        battery_values_vb.append(rr.vb)
        battery_values_vc.append(rr.vc)
        battery_values_vpv.append(rr.vpv) 
        
        #station information
        latititude = rr.latitude
        longitutde = rr.longitude
        station_name = rr.station_name
        depths = rr.depths
        #station info
        station_info = [station_id, station_name, latititude, longitutde, depths]

        #check if the key exists inside stations
        if station_id not in stations:
            stations[station_id] = [dates, moisture_values_m0, moisture_values_m1, moisture_values_m2, moisture_values_m3, 
                                    moisture_values_m4, temperature_values_t0, temperature_values_t1, temperature_values_t2, 
                                    temperature_values_t3, temperature_values_t4, battery_values_vb, battery_values_vc, 
                                    battery_values_vpv, station_info]
            
            
        else:
            #get the list, append it to a new list, add back to the location 

            #date update at index 0 in the dictionary 
            update_dictionary_list(station_id, 0, dates, stations)
            
            #all moisture values
            update_dictionary_list(station_id, 1, moisture_values_m0, stations)
            update_dictionary_list(station_id, 2, moisture_values_m1, stations)
            update_dictionary_list(station_id, 3, moisture_values_m2, stations)
            update_dictionary_list(station_id, 4, moisture_values_m3, stations)
            update_dictionary_list(station_id, 5, moisture_values_m4, stations)

            #all temperature values
            update_dictionary_list(station_id, 6, temperature_values_t0, stations)
            update_dictionary_list(station_id, 7, temperature_values_t1, stations)
            update_dictionary_list(station_id, 8, temperature_values_t2, stations)
            update_dictionary_list(station_id, 9, temperature_values_t3, stations)
            update_dictionary_list(station_id, 10, temperature_values_t4, stations)

            #all battery values 
            update_dictionary_list(station_id, 11, battery_values_vb, stations)
            update_dictionary_list(station_id, 12, battery_values_vc, stations)
            update_dictionary_list(station_id, 13, battery_values_vpv, stations)
        length = len(files)
        print(f'processed {count} daily files')

#now we need to go through each station and calcualte the percentiles / output a file
percentiles = list(range(0, 100, 1)) #list from 0 to 99th
for i in stations.keys():
    #grab the key and sort everything
    m0_percentiles = []
    m1_percentiles = []
    m2_percentiles = []
    m3_percentiles = []
    m4_percentiles = []
    t0_percentiles = []
    t1_percentiles = []
    t2_percentiles = []
    t3_percentiles = []
    t4_percentiles = []
    vb_percentiles = []
    vc_percentiles = []
    vpv_percentiles = []

    date = stations.get(i)[0][0]
    #get sorted date information 
    sorted_dates = sorted(date)
    #climatology dates
    first_known_date = sorted_dates[0]
    last_known_date = sorted_dates[-1]

    #lists to send for calculations 
    m0 = stations.get(i)[1][0]
    m1 = stations.get(i)[2][0]
    m2 = stations.get(i)[3][0]
    m3 = stations.get(i)[4][0]
    m4 = stations.get(i)[5][0]

    #temp 
    t0 = stations.get(i)[6][0]
    t1 = stations.get(i)[7][0]
    t2 = stations.get(i)[8][0]
    t3 = stations.get(i)[9][0]
    t4 = stations.get(i)[10][0]

    #battery 
    vb = stations.get(i)[11][0]
    vc = stations.get(i)[12][0]
    vpv = stations.get(i)[13][0]

    #station_info
    station_info = stations.get(i)[14]


    for j in percentiles:
        print(f'calculating {j} percentile for station {i}')
        m0_p = calculate_percentile(m0, j)
        m0_percentiles.append(m0_p)

        m1_p = calculate_percentile(m1, j)
        m1_percentiles.append(m1_p)

        m2_p = calculate_percentile(m2, j)
        m2_percentiles.append(m2_p)

        m3_p = calculate_percentile(m3, j)
        m3_percentiles.append(m3_p)

        m4_p = calculate_percentile(m4, j)
        m4_percentiles.append(m4_p)

        t0_p = calculate_percentile(t0, j)
        t0_percentiles.append(t0_p)

        t1_p = calculate_percentile(t1, j)
        t1_percentiles.append(t1_p)

        t2_p = calculate_percentile(t2, j)
        t2_percentiles.append(t2_p)

        t3_p = calculate_percentile(t3, j)
        t3_percentiles.append(t3_p)

        t4_p = calculate_percentile(t4, j)
        t4_percentiles.append(t4_p)

        vb_p = calculate_percentile(vb, j)
        vb_percentiles.append(vb_p)

        vc_p = calculate_percentile(vc, j)
        vc_percentiles.append(vc_p)

        vpv_p = calculate_percentile(vpv, j)
        vpv_percentiles.append(vpv_p)

    cwd = os.getcwd()
    climatology_dir = os.path.join(cwd, 'climatology_files')

    #make a directory for climatology files if needed
    if not os.path.exists(climatology_dir):
        os.mkdir(climatology_dir)

    #write out the file
    current_time = datetime.now()
    year = str(current_time.year)
    month = str(current_time.month)
    day = str(current_time.day)
    filename = i + "_" + year + month + day + '.txt'
    file = os.path.join(climatology_dir, filename)
    
    
    with open(file, 'w') as f:
            #write a header 
        stationid = station_info[0]
        stationname = station_info[1]
        stationlat = station_info[2]
        stationlon = station_info[3]
        stationdepth = station_info[4]

        f.write(f'id: {stationid}\n')
        f.write(f'name:  {stationname}\n')
        f.write(f'location: {stationlat} {stationlon}\n')
        f.write(f'depths: {stationdepth}\n')
        f.write(f'dates: {first_known_date}, {last_known_date}\n')
        f.write('\n')
        f.write('percentile, m0, m1, m2, m3, m4, t0, t1, t2, t3, t4, vpv, vb, vc\n')
        for x in range(len(percentiles)):
            f.write(str(x) + ', ' + str(m0_percentiles[x]) + ', ' + str(m1_percentiles[x]) + ', ' + str(m2_percentiles[x]) 
                    + ', ' + str(m3_percentiles[x]) +  ', ' + str(m4_percentiles[x]) +', ' + str(t0_percentiles[x]) + ', ' 
                    + str(t1_percentiles[x]) + ', ' + str(t2_percentiles[x]) + ', ' + str(t3_percentiles[x]) + ', ' + str(t4_percentiles[x]) 
                    + ', ' + str(vpv_percentiles[x]) + ', ' + str(vb_percentiles[x]) + ', ' + str(vc_percentiles[x])+'\n')

print('\n')
        
