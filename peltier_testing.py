import serial
import time
import qy
import numpy
from pprint import pprint
from heaters import heaters

'''
Code to set a voltage and periodically write the readings from the heaters to a file.  For electrical testing
'''

if __name__=='__main__':
    
    # Where to put to data
    output_file = open("test_write/test_data.csv", "w")

    #metadata={'label':'This is a test!', 'mood':'hungry for knowledge'}
    #output_file=ctx('/Users/jacquescarolan/Documents/PhD/Heater Code/test_write', metadata=metadata)
    
       
    # Create some heaters
    reck_heaters = heaters(port = '/dev/cu.usbserial')
    
    # Apply some voltages
    print reck_heaters.send_voltages([1,1,1,1,1,1,1,1])
    
    # Write results to a file
    output_file.write(reck_heaters.dict())
    
    
    
    # Shut it down
    print reck_heaters.zero()
    reck_heaters.kill()
 