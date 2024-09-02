
"""
Purpose: Contains helper funcitons that can be imported into other scripts.

"""
import datetime
import os

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
    mm = float(mm)
    vwc = 100.0 * ((4.824E-10*mm**3)-(2.28E-6*mm**2) + (3.898E-3 * mm) - 2.154)
    return str("{:.3f}".format(vwc)) #three decimal vwc
    
        
    