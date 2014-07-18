import time, sys
import serial
import qy
from qy.formats import ctx
import qy.settings
import numpy as np
from pprint import pprint
from heaters import heaters

'''
Code to set a voltage and periodically write the readings from the heaters to a file.  For electrical testing
'''

if __name__=='__main__':
    

	v = 1
	
	# Where to put to data
	metadata={'label':'Peltier Testing', 'test': 'apply voltage wait ten seconds then turn off, try 1v bias','voltages': v, 'peltier' : 'on'}
	output_file = ctx('C:/Users/Qubit/Desktop/Heater-Code/heat_10s_turnoff/Peltier_on/', metadata=metadata)

	# Number of steps, not heater.dict() takes 0.34 seconds to call = max rep rate
	steps = 50
	
	# Create some heaters
	reck_heaters = heaters(port = 'COM10')

	
	
	# Apply some voltages
	print reck_heaters.send_voltages([v,1,v,0,v,v,0,v])
	output_file.write('initial', reck_heaters.dict())
	time.sleep(10)
	
	# Start stop watch
	start = time.time()
	print reck_heaters.send_voltages([0,1,0,0,0,0,0,0])

	# Loop and save data to file with time stamp
	for time_step in range(0, steps):
		output_file.write(time.time()-start, reck_heaters.dict())
		#data.append(reck_heaters.dict())
		print 'got data %d out of %d' % (time_step+1, steps)
	
	
	print 'got it all!'
	
	
	# Shut it down
	print reck_heaters.zero()
	reck_heaters.kill()