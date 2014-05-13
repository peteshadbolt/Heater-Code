import serial
import time
import qy
import numpy

class heater:
    '''This class speaks to the heater driver through a serial port'''
    
    def __init__(self, port=None):
        '''Constructor for a heater object.'''
        print 'Connecting to heater driver...'
        self.serial=serial.Serial()
        self.serial.port=port
        self.serial.timeout=1
        self.baudrate=9600
        self.serial.bytesize=serial.EIGHTBITS
        self.serial.parity=serial.PARITY_NONE
        self.serial.stopbits=serial.STOPBITS_ONE
        self.heaters=8
        try:
            self.serial.open()
            print 'Connected.'
        except serial.SerialException:
            print 'Failed!'
            
#Serial excpetion doesn't work??

    def send_rcv(self, command):
        '''Send a single command and get a response'''
        self.serial.write(command + '\r\n')
        return_value = self.serial.readlines()
        return return_value[1]

    def send_v(self, list):
        '''Send multiple voltage commands and get a response'''
        if len(list)==self.heaters:
            for heater, voltage in enumerate(list):
                self.send_rcv('v%d=%d' % (heater, voltage))
            return 'voltages are %s' % (str(list))
        else:
            print 'I need %d voltages!' % (self.heaters)
    
    def send_i(self, list):
        '''Send multiple currents commands and get a response'''
        if len(list)==self.heaters:    
            for heater, current in enumerate(list):
                self.send_rcv('i%d=%d' % (heater, current))
            return 'currents are %s' % (str(list))
        else:
            print 'I need %d currents!' % (self.heaters)
            
    def send_p(self, list):
        '''Send multiple powers commands and get a response'''
        if len(list)==self.heaters:
            for heater, power in enumerate(list):
                self.send_rcv('p%d=%d' % (heater, power))
            return 'powers are %s' % (str(list))
        else:
            print 'I need %d powers!' % (self.heaters)
    
    def zero(self):
        '''zero all of the voltages'''
        self.send_rcv('vall=0')
        return 'all zero'
    
    def help(self):
        '''Help function'''
        command = 'help'
        self.serial.write(command + '\r\n')
        return_value = self.serial.readlines()
        for i in return_value:
            print i
    
    def query_all(self):
        '''print out all V,I,P'''
        command = 'vipall?'
        self.serial.write(command + '\r\n')
        return_value = self.serial.readlines()
        for i in return_value:
            print i
	
    def dict(self):
		'''dictionary for vip'''
		command = 'vipall?'
		self.serial.write(command + '\r\n')
		return_value = self.serial.readlines()
		i = 1
		voltages = []
		currents = []
		powers = []
		while i < len(return_value): 
			voltages.append(float(return_value[i].split()[1]))
			currents.append(float(return_value[i].split()[3]))
			powers.append(float(return_value[i].split()[5]))
			i+=1
		return {'voltages':voltages,'currents':currents,'powers':powers}
			
			
    def kill(self):
		'''Close the connection to the heater driver'''
		self.serial.close()
		print 'Disconnected from heater driver'

# TODO max PVI and test.  Another question -- do I want the code to output what it has done?  i.e. all set to blah blah blah


#TEST
if __name__=='__main__':

	#create a heater called test
	test = heater(port = 'COM10')

	print test.send_rcv('v1=1')

	test.send_v([1,1,1,1,1,1,1,0])

	test_dict=test.dict()
	print test_dict

	'''
					command = 'vipall?'
			self.serial.write(command + '\r\n')
			return_value = self.serial.readlines()
			return return_value[1].split()[1]
	'''

	print test.zero()
	#test.query_all()

	test.kill()