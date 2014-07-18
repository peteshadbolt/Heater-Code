import time, sys
import serial
import qy
from qy.formats import ctx
import qy.settings
import numpy as np
from pprint import pprint
from heaters import heaters

'''
Test for crosstalk between two neighbouring heaters. 
'''



if __name__=='__main__':
    
	# Set voltages to v
	v = 0
	v1 = 12
	v2 = 12
	# Where to put to data
	metadata={'label':'Crosstalk test', 'test': 'Set Voltages on nieghbouring heaters','voltages, try 1v bias': v, '22': v1, '23': v2, 'peltier' : 'on'}
	output_file = ctx('C:/Users/Qubit/Desktop/Heater-Code/Crosstalk/', metadata=metadata)

	# Number of steps, not heater.dict() takes 0.34 seconds to call = max rep rate
	steps = 50
	
	# Create some heaters
	reck_heaters = heaters(port = 'COM10')

	
	
	# Apply some voltages
	print reck_heaters.send_voltages([v,1,v,0,v1,v2,0,v])
	
	# Start stop watch
	start = time.time()

	# Loop and save data to file with time stamp
	for time_step in range(0, steps):
		output_file.write(time.time()-start, reck_heaters.dict())
		#data.append(reck_heaters.dict())
		print 'got data %d out of %d' % (time_step+1, steps)
	
	
	print 'got it all!'
	
	
	# Shut it down
	print reck_heaters.zero()
	reck_heaters.kill()