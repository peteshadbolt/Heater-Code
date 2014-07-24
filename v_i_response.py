import time, sys
import serial
import qy
from qy.formats import ctx
import qy.settings
import numpy as np
from pprint import pprint
from heaters import heaters
from matplotlib import pyplot as plt
import numpy as np

#### A test to monitor and display the volatge, current relation for a heater.

if __name__=='__main__':
    
    
    vmin = 0
    vmax = 12
    voltage_step = 0.5
    n =(vmax-vmin)/voltage_step
    loops = 10
    voltages = np.linspace(vmin,vmax,n+1)
    #heater_index = 18    
    
    
    
    
    # Create some heaters
    reck_heaters = heaters(port = 'COM10')
    #volts = []
    #currents = []
    # last heater + 1 for range
    heater_list = range(3,24)
    
    # Start the stopwatch
    start = time.time()
    for heater_index in heater_list:
        print 'HEATER INDEX IS %d'  %heater_index
        
        if heater_index == 4:
            print 'GND sensor'
            
        elif heater_index == 22:
            print 'GND sensor'
            
        else:
            metadata={'label':'Heater Testing', 'test': 'Apply a voltage to a heater in iuncrements and look and VvsI Beahaviour', 'Hetaer': heater_index, 'Loops': loops}
            output_file = ctx('C:/Users/Qubit/Data/reconfigurable_reck_callibration/electronic_test_data/', metadata=metadata)
            for v in voltages:
                
                reck_heaters.send_one_voltage(heater_index, v)
                       
                for j in range(loops):
                    print 'Loop %r out of %r' %(j+1, loops)
                    #output_file.write(time.time()-start, reck_heaters.vipall())
                    #out = reck_heaters.vip_heater(heater_index)
                    output_file.write(time.time()-start, reck_heaters.vip_heater(heater_index))
                    #volts.append(out[heater_index]['voltage'])
                    #currents.append(out[heater_index]['current'])
                    time.sleep(1)
            
            #plt.plot(volts, currents, 'x')
    
    reck_heaters.kill()
    
    #plt.savefig('C:/Users/Qubit/Data/reconfigurable_reck_callibration/electronic_test_data/'+str(time.time()))
    