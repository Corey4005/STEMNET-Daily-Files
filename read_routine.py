'''
This is a module to read daily files and dump the information 
into a class structure called ReadRoutine
'''

from datetime import datetime

class ReadRoutine:

    def __init__(self, filepath):
        self.file = filepath
        self.station_id = None 
        self.station_name = None
        self.latitude = None
        self.longitude = None
        self.depths = None
        self.observation_date = None #the daily file date
        self.observation_times = [] #list of observation times for the date
        self.m0 = [] # the first depth (top of soil) volumetric soil moisture 
        self.m1 = [] # 
        self.m2 = [] #  
        self.m3 = [] # 
        self.m4 = [] # # the last depth (last depth in soil)
        self.t0 = [] # the first depth (top of soil) temperature reading 
        self.t1 = [] #
        self.t2 = []
        self.t3 = []
        self.t4 = [] # the last depth (last in soil) temperature reading 
        self.vpv = [] #solar voltage (incoming)
        self.vb = [] #battery voltage
        self.vc = [] #clock battery voltage 
    
    def get_data(self):
        '''
        The purpose of this function is to read all of the data 
        in the daily file (self.filepath), and put this information 
        into lists that can be used for downstream analysis. 
        '''

        daily = open(self.file, 'r')
        
        linecount = 0
        for line in daily:
            line = line.split()
            #station id 
            if linecount == 0:
                self.station_id = line[1]
            #name
            elif linecount == 1:
                self.station_name = line[1]
            #location
            elif linecount == 2:
                self.latitude = line[1]
                self.longitude = line[2]
            #depths
            elif linecount == 3:
                self.depths = line[1]

            elif linecount == 4:
                self.observation_date = line[0]
            
            elif linecount >= 7:
                observation_time = line[0] + ' ' + line[1]
                self.observation_times.append(datetime.strptime(observation_time.rstrip(','), 
                                                                "%Y-%m-%d %H:%M:%S%f%z"))
                self.m0.append(float(line[2].rstrip(',')))
                self.m1.append(float(line[3].rstrip(',')))
                self.m2.append(float(line[4].rstrip(',')))
                self.m3.append(float(line[5].rstrip(','))) 
                self.m4.append(float(line[6].rstrip(',')))
                self.t0.append(float(line[7].rstrip(',')))
                self.t1.append(float(line[8].rstrip(',')))
                self.t2.append(float(line[9].rstrip(',')))
                self.t3.append(float(line[10].rstrip(',')))
                self.t4.append(float(line[11].rstrip(',')))
                self.vpv.append(float(line[12].rstrip(',')))
                self.vb.append(float(line[13].rstrip(',')))
                self.vc.append(float(line[14].rstrip(',')))
            
            linecount+=1



if __name__ == '__main__':
    ReadRoutine(testfile).get_data()
