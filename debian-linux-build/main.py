"""
Purpose: a script to drive the data infrustructure process.

"""
import subprocess
import time
import os 
from datetime import datetime
def main():
    # make sure the directories exist if they do not already 
    current_date = datetime.now()
    print(f'main.py call: {current_date}\n')
    cwd = os.getcwd()
    daily_files_dir = os.path.join(cwd, 'daily_files')
    logfiles_dir = os.path.join(cwd, 'logfiles')
    last_station_times_dir = os.path.join(logfiles_dir, 'last_station_times')
    station_data_dir = os.path.join(cwd, 'station_data')
    metadata_dir = os.path.join(cwd, 'metadata')
    data_out_dir = os.path.join(cwd, 'data_out')

    if not os.path.exists(daily_files_dir):
        os.mkdir(daily_files_dir)
    if not os.path.exists(logfiles_dir):
        os.mkdir(logfiles_dir)
    if not os.path.exists(last_station_times_dir):
        os.mkdir(last_station_times_dir)
    if not os.path.exists(station_data_dir):
        os.mkdir(station_data_dir)
    if not os.path.exists(metadata_dir):
        os.mkdir(metadata_dir)
    if not os.path.exists(data_out_dir):
        os.mkdir(data_out_dir)

    start = time.time()
    #fetch the updated metadata and all available soil moisture data
    subprocess.run(['python', './get_data.py'])
    
    #process daily files
    subprocess.run(['python', './process_daily.py'])
    
    #rsyncing data to out dir
    subprocess.run(['./move_script.sh'])    
    #measure run time
    end = time.time()
    script_time = end - start
    print(f'Total process time: {script_time}\n')
    return None

if __name__ == '__main__':
    main()
    
