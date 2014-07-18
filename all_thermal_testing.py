import time, sys
import serial
import qy
from qy.formats import ctx
import qy.settings
import numpy as np
from pprint import pprint
from heaters import heaters

'''
Take samples with no voltage, take samples with voltage, take samples no voltage.  All heaters active
'''

if __name__=='__main__':
    

	v = 12
	bias = 1
	
	# Where to put to data
	metadata={'label':'Peltier Testing', 'test': 'complete heater test. no voltage. voltage. no voltage','voltages': v, 'peltier' : 'on'}
	output_file = ctx('C:/Users/Qubit/Code/lab_code/Heater-Code/electronic_testing_all_heaters/Peltier_on', metadata=metadata)
	
	# Create some heaters
	reck_heaters = heaters(port = 'COM10')
	
	# Start the stopwatch
	start = time.time()
	
	# Turn thermistor on
	print reck_heaters.send_voltages([0,0,bias,0,0,0,0,0])
	
	# Take samples with no voltages
	# Loop and save data to file with time stamp
	for time_step in range(0, 10):
		output_file.write(time.time()-start, reck_heaters.dict())
		print 'no heat: got data %d out of %d' % (time_step+1, 10)
	
	# Turn voltages on
	print reck_heaters.send_voltages([0,0,bias,v,0,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,0,v,])
	
	# Take samples with applied voltages
	for time_step in range(0, 30):
		output_file.write(time.time()-start, reck_heaters.dict())
		print 'turning on the heat: got data %d out of %d' % (time_step+1, 30)
	
	# Turn voltages off
	v = 0
	print reck_heaters.send_voltages([0,0,bias,v,0,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,0,v,])
	
	# Take samples with voltages off voltages
	for time_step in range(0, 30):
		output_file.write(time.time()-start, reck_heaters.dict())
		print 'turning off the heat: got data %d out of %d' % (time_step+1, 30)
	
	
	print reck_heaters.zero()
	reck_heaters.kill()
	
