import time, sys
import serial
import qy
from qy.formats import ctx
import qy.settings
import numpy as np
from pprint import pprint
from heaters import heaters


if __name__=='__main__':

    reck_heaters = heaters(port = 'COM10')
    v = 5
    bias = 1
    print reck_heaters.send_voltages([0,0,bias,v,0,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,v,0,v,])
    print reck_heaters.query_i(2)
    
    print reck_heaters.vip_heater(2)
    
    #print reck_heaters.dict()
    
    print '\n'
    #print reck_heaters.vipall()
    
    print reck_heaters.zero()
    reck_heaters.kill()