"""
Purpose: a script to drive the data infrustructure process.

"""
import subprocess
import time

def main():
    start = time.time()
    #fetch the updated metadata and all available soil moisture data
    subprocess.run(['python', './get_data.py'])
    
    #process daily files
    subprocess.run(['python', './process_daily.py'])
    
    #measure run time
    end = time.time()
    script_time = end - start
    print(f'Total process time: {script_time}')
    return None

if __name__ == '__main__':
    main()
    