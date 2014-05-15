import time, sys
import serial
import qy
from qy.formats import ctx
import qy.settings
import numpy as np
from pprint import pprint
from heaters import heaters

'''
Inital testing
'''

if __name__=='__main__':
	
	# Where to put to data
	metadata={'label':'Peltier Testing', 'test':'thermistor characterisation', 'temperature': '20.00', 'notes': 'thermistor on heater 01, bias at 10V'}
	output_file = ctx('C:/Users/Qubit/Desktop/Heater-Code/thermistor_characterisation/', metadata=metadata)

	
	
	reck_heaters = heaters(port = 'COM10')
	
	print reck_heaters.send_voltages([0,10,0,0,0,0,0,0])
	pprint(reck_heaters.dict())
	output_file.write('20.00', reck_heaters.dict())

	
	print reck_heaters.zero()
	reck_heaters.kill()