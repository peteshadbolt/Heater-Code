
class dac:
    def __init__():
        connect to the hardware
        check everything works
        
    def write_voltages(index, voltage)
    
    def zero()

    
class calibration_table:
    def __init__(filename)
        loads up the table
    
    def get_voltage(phase)
    
    def get_voltages()
    

class counting:
    def get_counts()
    
class heaters:
    def __init__(filename)
        self.dac=dac()
        self.table=calibration_table(filename)
        
    def set_phases(phases)
        voltages=self.calibration_table.get_voltages(phases)
        self.dac.set_voltages(voltages)
        
    def zero()
        self.dac.zero()
        
        
#main important experiment running code
        
def pulse(phases, heater_device, counting_device)
    #turn on the heaters
    heater_device.set_phases(phases)
    time.sleep(1 second)  #heat up
    counts = counting_device.count(1 second)
    heater_device.zero()
    time.sleep(1 second)  #cool down    
    return counts        

h=heaters()
c=counting()
counts = pulse([0,0,0,0,0,0], h, c)
        