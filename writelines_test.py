import serial

# note can't run this in texmate, need to run in terminal, use command + shift + R

# open the serial port on my mac
ser = serial.Serial(\
                    '/dev/cu.usbserial', \
                    9600, \
                    timeout=0.01, \
                    parity=serial.PARITY_NONE, \
                    bytesize=serial.EIGHTBITS, \
                    stopbits=serial.STOPBITS_ONE\
                    )
# check the location
print ser.name

'''
ser.write('v1=5')

ser.flushOutput()

ser.write('v0=5')

ser.flushOutput()
'''

#response = ser.readlines()
#for x in response:
#    print x

def send_rcv(x):
    

ser.write('v1=5')

ser.write('vipall?\n')

response = ser.readlines()
for x in response:
    print x




ser.close









