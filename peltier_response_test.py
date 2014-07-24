import time, sys
import serial
import qy
from qy.formats import ctx
import qy.settings
import numpy as np
from pprint import pprint
from heaters import heaters

'''
Turn on all heaters to 12v, monitor for an extened period of time. To be tested with peltier off, 
and also initially off and the on halfway through.
'''

if __name__=='__main__':
    

	v = 5
	bias = 10
	
	# Where to put to data
	metadata={'label':'Peltier Testing', 'test': 'complete heater test. just apply voltage, observe change in temp ','voltages': v, 'peltier' : 'off'}
	output_file = ctx('C:/Users/Qubit/Code/lab_code/heater_testing/peltier_response_tests/Peltier_off', metadata=metadata)
	
	# Create some heaters
	reck_heaters = heaters(port = 'COM10')
	
	# Start the stopwatch
	start = time.time()
	
	# Turn voltages on
	print reck_heaters.send_voltages([0,0,bias,v,0,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,0,v,])
	
	# Take samples with applied voltages
	for time_step in range(0, 1000):
		output_file.write(time.time()-start, reck_heaters.dict())
		print 'turning on the heat: got data %d out of %d' % (time_step+1, 1000)
	
	
	
	print reck_heaters.zero()
	reck_heaters.kill()
	
