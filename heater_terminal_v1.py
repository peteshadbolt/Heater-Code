import serial

# note can't run this in texmate, need to run in terminal, use command + shift + R

# open the serial port on my mac
ser = serial.Serial(\
                    '/dev/cu.usbserial', \
                    9600, \
                    timeout=1, \
                    parity=serial.PARITY_NONE, \
                    bytesize=serial.EIGHTBITS, \
                    stopbits=serial.STOPBITS_ONE\
                    )
# check the location
print ser.name


print 'Enter your commands below.\r\nInsert "exit" to leave the application.'


# get raw keyboard input (note that while loop will run forever unless exit is called)

while True :
    input = raw_input(">> ")
    if input == 'exit':
        ser.close
        exit()
    else:
        ser.write(input + '\r\n')
        response = ser.readlines()
        for x in response:
            print x
