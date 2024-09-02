
"""
Pupose: A script to take in all csv soil moisture files and process
    them into daily soil moisture observations or daily files. 
"""

import csv
import os
import re
import logging
import subprocess
import datetime
from helper_functions import try_epoch_to_date
from helper_functions import create_header
from helper_functions import calculate_vwc


#for each csv in the station_data folder:
station_data_dir = os.getcwd() + '/station_data/'
processed_stations = [] #the stations that make it all the way through the process
fail_stations = [] # a dictonary to output to error log
only_fail_stations_name = [] # a list to keep up with just the names of the fail stations

#set up a log file
logging.basicConfig(filename='error.log', filemode='w')
#script to move log file
movescript = './movelog.sh'

#station metadata
metadata = './metadata/sn_meta.txt'

for fn in os.listdir(station_data_dir):
    # get the filename and append to working dir
    if fn.endswith('csv'):
        file_path=os.path.join(station_data_dir,
                               fn)
        
        # 1. identify the station, open the file.
        station = fn.split('.')[0]
        # getting the metadata
        with open(metadata) as metafile:
            reader = csv.DictReader(metafile)
            for r in reader:
                if r['id'] == station:
                    latitude = r['latitude']
                    longitude = r['longitude']
                    name = r['name']
                    depths = r['depths']
                    
        # 2. loop through the csv and grab the data and time column, append this together to a list
        with open(file_path) as file:
            reader = csv.DictReader(file)
            #convert the data to a list of dictionaries
            data = list(reader)
            has_data = bool(data) #flag to check that there is data in the file
            all_columns_available = True #assume all columns available
            
            #check for all columns in the data:
            if has_data:
                for i in ['t0','t1','t2','t3','t4','vpv','vb','vc','m0','m1','m2','m3','m4','time']:
                #if one is not available, then turn the all_columns_available flag to false
                    if i in data[0]:
                        pass
                    else:
                        all_columns_available = False
            
            # 3. sort the list of timestamps along with the data
            if has_data and all_columns_available: #make sure that we actually got data in the file and the column for time exists
                print(f'Processing {station} Daily Files')
                sorted_data = sorted(data, key=lambda x: x['time'], reverse=False)
                #go through the sorted data and check each timestamp for greater than or less than 10 character timestamp. Remove an observation that violates.
                length_bad_time_data = [record['time'] for record in sorted_data if len(str(record['time']))!=10]
                #get the bad data that has any other character and not already in longbad_time_data
                pattern = re.compile(r'\D') #regex for string that contains non-numeric characters
                #but do not append anything already found above in longbad_time_data
                nonnumericbad_data = [record['time'] for record in sorted_data if pattern.search(record['time']) and record['time'] not in length_bad_time_data]
                #go through and find the index with matching records
                #all bad records to log and 
                all_bad = length_bad_time_data + nonnumericbad_data
                #create a list without the bad data 
                cleaned_records = [record for record in sorted_data if record['time'] not in all_bad]
    
                if len(all_bad)>0:
                    logging.warning(f'[BAD TIME DATA, BAD LENGTH OR NON-NUMERIC], {station}, {all_bad}')
                
            else:
                fail_stations.append({'station': station,
                                      'has_all_columns': all_columns_available,
                                      'has_data': has_data})
                only_fail_stations_name.append(station)
                pass
            
            # 4. identify if a "last known timestamp" exists in the last_station_times/{station}.csv file.
            #last known station data file:
            last_known_observations = os.getcwd() + f'/logfiles/last_station_times/{station}.csv'
            #only check for stations not in the fail station list
            #if it doesn't exist, this is the first time the system has operated on a station
            # and the files need to be set up for it to track for later use. 
            if not os.path.exists(last_known_observations) and station not in only_fail_stations_name:
                with open(last_known_observations, 'w') as obs:
                    writer = csv.writer(obs) #collecting all into a list
                    lasttimestamp = [
                        ['station', 'time'],
                        [station, cleaned_records[-1]['time']] #we put the last record in the file, in the future we start here
                                     ]
                    
                    writer.writerows(lasttimestamp)
                    #in this case, we need to start from the first record we have, because a tracked file does not
                    #exist yet.
                    first_processed_time = cleaned_records[0]['time']
                    last_processed_time = cleaned_records[-1]['time']
                    records_to_create = [record for record in cleaned_records if record.get('time') > first_processed_time]
            
            elif os.path.exists(last_known_observations) and station not in only_fail_stations_name:        
            # 6. for each timestamp after a last known timestamp, do 7
                with open(last_known_observations, 'r') as obs:
                    reader = csv.DictReader(obs) #collecting all into a list
                    for r in reader:
                        last_processed_time = r['time'] #getting the last known time 
                    
                    #get the index of the last processed time
                    records_to_create = [record for record in cleaned_records if record.get('time') > last_processed_time]
                
                #overwriting the last known time
                with open(last_known_observations, 'w') as obs:
                    writer = csv.writer(obs) #collecting all into a list
                    lasttimestamp = [
                        ['station', 'time'],
                        [station, cleaned_records[-1]['time']] #we put the last record in the file, in the future we start here
                                     ]
                    writer.writerows(lasttimestamp)
                    
            # 7. check if a station folder exists and a year directory exists for that time stamp in the station folder.
            station_dir = os.getcwd() + f'/daily_files/{station}'
            bad_epoch_dictionary = {} #dictionary to store bad epoch values by station
            if not os.path.isdir(station_dir):
            #a. if the station folder does not exist, make a station and year directory
                os.mkdir(station_dir)
            
            #create a timestamp for each time in the records, return 999 for a problem timestamp
            clean_timestamps = [try_epoch_to_date(record, station, bad_epoch_dictionary) for record in records_to_create]
            
            #if there was a bad epoch time, log it. 
            if station in bad_epoch_dictionary:
                logging.error(f'[DATE CONVERSION ERROR {station}: {bad_epoch_dictionary.get(station)}')
            
            #b. for each timestamp in the clean records, check for a folder with the year and day.
            for i in clean_timestamps:
                bad_vwc = {} #log any vwc below zero 
                
                if i=='999':
                    pass
                    #do nothing
                else:
                    #set the date variables from the record
                    year = i.get('time').year
                    day = '{:02d}'.format(i.get('time').day)
                    month = '{:02d}'.format(i.get('time').month)
                    hour = i.get('time').hour
                    minute = i.get('time').minute
                    second = i.get('time').second
                    
                    #check if the dir exists
                    if os.path.exists(station_dir +'/'+str(year)):
                        pass
                
                    else:
                    #else make the dir
                        os.mkdir(station_dir +'/'+str(year))
                
                
                    #same with the month dir
                    if os.path.exists(station_dir +'/'+str(year) + '/'+str(month)):
                        pass
                
                    else:
                        os.mkdir(station_dir +'/'+str(year) + '/'+str(month))
                    
                
                    #same with the day dir
                    if os.path.exists(station_dir +'/'+str(year) + '/'+str(month) + '/' +str(day)):
                        pass
                
                    else:
                        os.mkdir(station_dir +'/'+str(year) + '/'+str(month) + '/' +str(day))
                
                    #now we will check if the file exists, write out the data
                    if os.path.exists(station_dir +'/'+str(year) + '/'+str(month) + '/' +str(day) + '/' + f'{year}{month}{day}.txt'):
                        with open(station_dir +'/'+str(year) + '/'+str(month) + '/' +str(day) + '/' + f'{year}{month}{day}.txt', 'a') as file:
                            time = i.get('time')
                            #soil moisture values
                            m0 = calculate_vwc(i.get('m0'))
                            m1 = calculate_vwc(i.get('m1'))
                            m2 = calculate_vwc(i.get('m2'))
                            m3 = calculate_vwc(i.get('m3'))
                            m4 = calculate_vwc(i.get('m4'))
                            #temps
                            t0 = i.get('t0')
                            t1 = i.get('t1')
                            t2 = i.get('t2')
                            t3 = i.get('t3')
                            t4 = i.get('t4')
                            #sensor info
                            vpv = i.get('vpv')
                            vb = i.get('vb')
                            vc = i.get('vc')
                            
                            file.write(f'{time}, {m0}, {m1}, {m2}, {m3}, {m4}, {t0}, {t1}, {t2}, {t3}, {t4}, {vpv}, {vb}, {vc}\n')
                
                    else:
                        with open(station_dir +'/'+str(year) + '/'+str(month) + '/' +str(day) + '/' + f'{year}{month}{day}.txt', 'w') as file:
                            #write the id of station
                            file.write(f'id: {station}\n')
                            #write station name
                            file.write(f'name: {name}\n')
                            #latitude, longitude
                            file.write(f'location: {longitude}, {latitude}\n')
                            # depths
                            file.write(f'depths: {depths}\n')
                            # date
                            file.write(f'{month}-{year}-{day}\n')
                            #column headers
                            file.write('\n')
                            file.write(create_header()+'\n')
                            #data 
                            time = i.get('time')
                            #soil moisture values
                            m0 = calculate_vwc(i.get('m0'))
                            m1 = calculate_vwc(i.get('m1'))
                            m2 = calculate_vwc(i.get('m2'))
                            m3 = calculate_vwc(i.get('m3'))
                            m4 = calculate_vwc(i.get('m4'))
                            #temps
                            t0 = i.get('t0')
                            t1 = i.get('t1')
                            t2 = i.get('t2')
                            t3 = i.get('t3')
                            t4 = i.get('t4')
                            #sensor info 
                            vpv = i.get('vpv')
                            vb = i.get('vb')
                            vc = i.get('vc')
                            #write out all values 
                            file.write(f'{time}, {m0}, {m1}, {m2}, {m3}, {m4}, {t0}, {t1}, {t2}, {t3}, {t4}, {vpv}, {vb}, {vc}\n')
                            

#log the bad timestamps:
logging.error(f'[FILE READ ERRORS, MISSING COLUMNS OR MISSING DATA], {fail_stations}')
subprocess.run([movescript])