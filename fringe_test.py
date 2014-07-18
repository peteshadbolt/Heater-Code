import time, sys
import serial
from qy.hardware.dpc230 import coincidence_counter
from qy.formats import ctx
from qy.hardware import smc100
import qy.settings
import numpy as np

from heater_class import heater

if __name__=='__main__':

	def handle_data(data):
			''' Define how to handle data coming from the counting system '''
			key, value = data
			#print data
			if key=='coincidence_data':
				# We got some count rates
				count_rates=value['count_rates']
				# together with the context in which they were measured
				context=value['context']
			
				# Print out some stuff
				print 'Recieved data for heater setting %s' % str(context[0])
				if 'n' in count_rates: print 'n: %d' % count_rates['n']
				
				# Write full context information to disk
				output_file.write('Heater context', context)
				# A less verbose alternative: 
				# output_file.write('position', context[which_motor]['position'])
				# Write count rates to disk
				output_file.write('count_rates', count_rates)

	##################################################### 
	# START HERE 
	##################################################### 

	# Get a file ready to store data
	metadata={'label':'This is a test!', 'mood':'hungry for knowledge'}
	output_file=ctx('C:/Users/Qubit/Desktop/data_from_example_scripts/', metadata=metadata)

	# 	Voltage parameters
	v1 = [1,0,0,0,0,0,0,0]
	v2 = [2,0,0,0,0,0,0,0]
	v3 = [3,0,0,0,0,0,0,0]
	v4 = [4,0,0,0,0,0,0,0]
	v_list = [v1, v2, v3, v4]

	# Connect to the heaters
	test_heaters = heater(port = 'COM10')

	# Connect to the counting gear and configure it
	counter=coincidence_counter(callback=handle_data)
	counter.set_integration_time(1)

	for voltage in v_list:
		print 'Setting voltage %s' % str(voltage)
		test_heaters.send_v(voltage)
		current_context=test_heaters.dict()
		counter.count(context=current_context)

	# Collect and log the last piece of data from the postprocessor
	counter.collect()

	# Close connections to hardware
	counter.kill()
	test_heaters.kill()
			