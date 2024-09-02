
"""
Purpose: A script to pull down the up-to-date metadata file and
    pull all available soil moisture data. The bash scripts
    get_metadata.sh and get_station.sh are required. 
"""

import csv
import subprocess
import sys

#make sure the metadata file is up to date
metadata_script = "./get_metadata.sh" #script to get the metadata
stationdata_script = "./get_station.sh" #script to get the current station data

try:
    subprocess.run([metadata_script], check=True, text=True, capture_output=True)
    
    #open the metadatafile and begin fetching the the csv files
    print('fetching all station csv files\n')
    with open ("./metadata/sn_meta.txt") as file:
        reader = csv.DictReader(file)
        for r in reader:
            for c, v in r.items():
                #find the id and if it exists, make a call to get the csv file
                if c=='id':
                    #call the station script
                    print(f'fetching {v}')
                    args = [v] #putting arg 1 in the list to pass to the bash script
                    try:
                        result = subprocess.run([stationdata_script] + args, check=True, text=True, capture_output=True)
                        print(f'	 success\n')
                    except:
                        print(f'	 failed\n')
                        pass #passing this v in the loop to try the next station
                    
    print('All possible data downloaded.')
except:
    print('Could not collect updated metadata. Exiting!')
    sys.exit(1) 