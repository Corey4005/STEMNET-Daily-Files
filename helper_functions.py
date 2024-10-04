
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
            
            #check the number of sensors 
            num_sensors = check_depths(depths)

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
                            write_row(i, file, num_sensors)
                
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
                            #write to the file
                            write_row(i, file, num_sensors)

def update_dictionary_list(station_id, index, list_to_add, dictionary):
    """
    Purpose: 
        updates a dictionary list at a particular value index for a particular 
        station key.          
    """
    #grabbing the current list at index in the dictionary
    list = dictionary.get(station_id)[index][0]

    #creating a new list by appending defined list to current list
    newlist = [*list, *list_to_add[0]]

    #updating dictionary values
    dictionary.get(station_id)[index][0] = newlist
    

def calculate_percentile(list, percentile):
    """
    calculates the percentiles   
    """
    #remove 999
    # Remove all occurrences of -999.99
    filtered_list = [x for x in list if x != -999.99]

    #if all values are -999.99
    if len(filtered_list) == 0:
        return -999.99
    #if length is less than 99, then you cant get a percentile 
    #Step 1: Count the total numbers of values in the given data set as n
    count = len(filtered_list)
    # Step 2: Rank the values in the given data set in ascending order that is rank them from least to greatest.
    list = sorted(filtered_list)
    # Step 3: To find the pth percentile multiply the p% or p/100 x n The answer that we get after multiplying is called index.
    index = percentile/100 * count
    # Step 4: Round the index to the nearest whole number if it is in decimal.
    index = round(index)

    if index >= count: #error with number of observations
        return -999.99 
    # Step 5: Identify the desired pth percentile asked in the problem. Count the values in the data set until we reach the index value. 
    # The number that corresponds to that value is the pth percentile. 
    return list[index]


def check_depths(depths):
    """
    Purpose: splits the depths into a list 
    returns the length of the depths parameter 
    """
    listdepths = depths.split(';')
    return len(listdepths)


def write_row(timestamp, file, num_sensors):
    """
    writes the soil moisture and temperature values 
    to the file and makes sure values are real 
    by putting in -999.99 if the depth does not 
    technically exist 
    """
    #get the data from the dictionary for time
    time = timestamp.get('time')

    if num_sensors < 1:
        #if sensors are less than 1, then there are no depth observations
        #and everything should be nan
        m0 = "-999.99"
        m1 = "-999.99"
        m2 = "-999.99"
        m3 = "-999.99"
        m4 = "-999.99"

        t0 = "-999.99"
        t1 = "-999.99"
        t2 = "-999.99"
        t3 = "-999.99"
        t4 = "-999.99"
    
    elif num_sensors == 1:
        #one soil moisture and 
        m0 = calculate_vwc(timestamp.get('m0'))
        #one temperature obs 
        t0 = timestamp.get('t0')

        #everything else 999
        m1 = "-999.99"
        m2 = "-999.99"
        m3 = "-999.99"
        m4 = "-999.99"

        t1 = "-999.99"
        t2 = "-999.99"
        t3 = "-999.99"
        t4 = "-999.99"

    elif num_sensors == 2:
        #2 sm obs and 
        m0 = calculate_vwc(timestamp.get('m0'))
        m1 = calculate_vwc(timestamp.get('m1'))
        #2 temp obs
        t0 = timestamp.get('t0')
        t1 = timestamp.get('t1')
        
        #everything else 999
        m2 = "-999.99"
        m3 = "-999.99"
        m4 = "-999.99"
        
        t2 = "-999.99"
        t3 = "-999.99"
        t4 = "-999.99"

    elif num_sensors == 3:
        # 3 sm obs 
        m0 = calculate_vwc(timestamp.get('m0'))
        m1 = calculate_vwc(timestamp.get('m1'))
        m2 = calculate_vwc(timestamp.get('m2'))
        # 3 temp obs
        t0 = timestamp.get('t0')
        t1 = timestamp.get('t1')
        t2 = timestamp.get('t2')

        m3 = "-999.99"
        m4 = "-999.99"

        t3 = "-999.99"
        t4 = "-999.99"
    
    elif num_sensors == 4: 
        #4 sm obs and 
        m0 = calculate_vwc(timestamp.get('m0'))
        m1 = calculate_vwc(timestamp.get('m1'))
        m2 = calculate_vwc(timestamp.get('m2'))
        m3 = calculate_vwc(timestamp.get('m3'))

        # 4 temp obs
        t0 = timestamp.get('t0')
        t1 = timestamp.get('t1')
        t2 = timestamp.get('t2')
        t3 = timestamp.get('t3')

        #everything else 999
        m4 = "-999.99"
        t4 = "-999.99"

    elif num_sensors == 5:
        #get everything at all depths
        #5 sm obs and 
        m0 = calculate_vwc(timestamp.get('m0'))
        m1 = calculate_vwc(timestamp.get('m1'))
        m2 = calculate_vwc(timestamp.get('m2'))
        m3 = calculate_vwc(timestamp.get('m3'))
        m4 = calculate_vwc(timestamp.get('m4'))
        # 5 temp obs
        t0 = timestamp.get('t0')
        t1 = timestamp.get('t1')
        t2 = timestamp.get('t2')
        t3 = timestamp.get('t3')
        t4 = timestamp.get('t4')

    else:
        return #what the heck is going on?, dont write anything

    #sensor info
    vpv = timestamp.get('vpv')
    vb = timestamp.get('vb')
    vc = timestamp.get('vc')
    
    file.write(f'{time}, {m0}, {m1}, {m2}, {m3}, {m4}, {t0}, {t1}, {t2}, {t3}, {t4}, {vpv}, {vb}, {vc}\n')