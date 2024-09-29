
"""
Purpose: Contains helper funcitons that can be imported into other scripts.

"""
import datetime
import os
from datetime import timedelta

def try_epoch_to_date(record, station, bad_time_dictionary):
    """
    Purpose: Converts epoch to UTC, or appends epoch value to station key if it cannot covert it.
    
    Parameters:
        record: dictionary containing the soil moisture data at a particular timestamp
        station: string representing the station name
        bad_time_dictionary: a dictionary containing station key and values of bad times
        
    Returns:
    
        Updated dictionary with a time period from 1970-01-01 00:00:00 updated to UTC time. 
        
    """
    try:
        #try to create a datestamp
        epoch = record.get('time')
        datestamp = datetime.datetime.fromtimestamp(int(epoch), datetime.timezone.utc)
        record['time'] = datestamp
        return record
    
    except:
        #except if the datestamp returns an error
        if station in bad_time_dictionary:
            #check if the key value pair exists for a particular station
            
            #if it does, append the epoch
            bad_time_dictionary[station].append(record)
        
        #else if it doesn't exist
        else:
            #creating the station key, value pair, then append
            bad_time_dictionary[station] = []
            bad_time_dictionary[station].append(record)
            
        return '999'
    
        
def create_header():
    """
    Purpose: to create the header columns in a new daily file
    """
    
    columns = 'Date, m0, m1, m2, m3, m4, t0, t1, t2, t3, t4, vpv, vb, vc'
    

    return columns 
    

def calculate_vwc(mm):
    """
    Purpose: to calculate volumetric water content from a voltage
    
    parameters:
    mm - the voltage to convert to volumetric water content
    """
    if mm == "-999.99":
        return mm
    
    else:
        mm = float(mm)
        vwc = 100.0 * ((4.824E-10*mm**3)-(2.28E-6*mm**2) + (3.898E-3 * mm) - 2.154)
        if vwc > 0.0:
            return str("{:.3f}".format(vwc)) #three decimal vwc
        else:
            return "-999.99" #cleans data that is below 0 volts
    
def check_timestamp(epoch):
    """
    Purpose: this function compares a timestamp to the current date and
    returns timestamps that are greater than UTC + 12, the current time
    at the farthest UTC location on Earth. Anything over this time
    would suggest a timestamp error because the clocks on the
    sensor cannot be greater than what is currently possible on earth.
    
    """
    try: 
        datestamp = datetime.datetime.fromtimestamp(int(epoch), datetime.timezone.utc)
        now = datetime.datetime.now(datetime.timezone.utc) + timedelta(hours=12)
        if datestamp > now:
            return epoch 
        #returns none if datestamp is less than now (UTC + 12) 
        
    except:
        return epoch
    

def process_daily(station, logging, records_to_create, longitude, latitude, name, depths):
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