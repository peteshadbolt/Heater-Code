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

	# Create some heaters
	reck_heaters = heaters(port = 'COM10')
	
	v=1
	bias=1
	print reck_heaters.send_voltages([0,0,bias,v,0,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,0,v,])
	print reck_heaters.dict()
	
	print reck_heaters.send_rcv('v18?')
	
	print reck_heaters.zero()
	reck_heaters.kill()
	
	


