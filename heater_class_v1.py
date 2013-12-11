import serial
import time
import qy

class heater:
    '''This class speaks to the heater driver through a serial port'''
    
    def __init__(self, port=None):
        '''Constructor for a heater object.'''
        print 'Connecting to heater driver...'
        self.serial=serial.Serial()
        self.serial.port=port
        self.serial.timeout=0.1
        self.baudrate=9600
        self.serial.bytesize=serial.EIGHTBITS
        self.serial.parity=serial.PARITY_NONE
        self.serial.stopbits=serial.STOPBITS_ONE
        try:
            self.serial.open()
            print 'Connected.'
        except serial.SerialException:
            print 'Failed!'
    
    def send_rcv(self, command):
        '''Send a command and get a response'''
        self.serial.write(command + '\r\n')
        return_value = self.serial.readlines()
        return return_value[1]
    
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
    
    def kill(self):
        '''Close the connection to the heater driver'''
        print 'Disconnected from heater driver'

#create a heater called test
test = heater(port = '/dev/cu.usbserial')

test.send_rcv('v0=0')
test.send_rcv('v1=0')
test.send_rcv('v2=0')
test.send_rcv('v3=0')
test.send_rcv('v4=0')



print test.query_all()


test.kill()