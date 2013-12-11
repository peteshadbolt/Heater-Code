import qy
from bayes import bayes_update
counted_file_writer=qy.hardware.counting.counted_file_writer    # alias counted_file


class experiment:
	def __init__(self):
		# connect to the motor controller
		self.smc100=qy.hardware.smc100(callback=self.motor_callback)
		print self.smc100
		
		# connect to the flipper
		self.flipper=qy.hardware.flipper_mount()

		# connect to the dpc230
		self.photon_buffer_1=qy.settings.lookup('photon_buffer_1')
		self.dpc230=qy.hardware.counting.dpc_daq(callback=self.counting_callback)
		print self.dpc230.print_board_summary()
		
		# build a counted file object and set defaults
		# this is the object which converts timetags to coincidences
		self.integration_time_ms=1000
		counted_filename='data.counted'
		counted_file_writer.new_counted_file(counted_filename)
		counted_file_writer.set_window(30)
		counted_file_writer.set_time_cutoff_ms(self.integration_time_ms)
		self.set_delays(map(int, qy.settings.lookup('delays').split(',')))
				
	def set_delays(self, new_delays):
		''' write a new set of delays '''
		d=counted_file_writer.array(16)
		for i in range(16):
			d[i]=new_delays[i]
		counted_file_writer.set_delays(d)
		
	def set_integration_time(self, new_time):
		''' set the integration_time '''
		self.integration_time_ms=new_time
		counted_file_writer.set_time_cutoff_ms(self.integration_time_ms)

	def run_experiment(self):
		''' the main experimental program '''
		# initialize a bayesian updater object
		self.bayes=bayes_update()
		
		# loop
		for i in range(3):
			self.update_once()
			
	def update_once(self):
		''' a single update '''
        
		# measure timetags for one second
		counted_file_writer.start_integrating()
		tdc1, tdc2 = self.dpc230.count(self.photon_buffer_1, self.integration_time_ms/1000.)
		spc_filename = self.dpc230.convert_raw_data(tdc1, tdc2)
		
		# convert timetags to coincidences
		counted_file_writer.process_spc(spc_filename)
		counted_file_writer.stop_integrating(0)

		# extract some numbers of interest
		pattern1=(0,1)
		pattern2=(1,0)
		print '01', counted_file_writer.get_number_rate_8x2(*pattern1)
		print '10', counted_file_writer.get_number_rate_8x2(*pattern2)
		all_counts=(1,2,3)
		
		# send stuff off to bayes
		self.bayes.send_counts(all_counts)
		self.bayes.update()
		self.move_motor_controller(3, self.bayes.get_new_control_phase())
		if self.bayes.get_flipper(): self.flipper.pulse()
		self.set_integration_time(self.bayes.get_integration_time())
				
		# look at the state afterwards
		print self.smc100.actuators[0].position

	def motor_callback(self, message):
		''' the motors did something '''
		pass
		
	def counting_callback(self, message):
		''' the counting system did something '''
		pass
		
	def move_motor_controller(self, mc_index, position):
		''' move a motor controller '''
		self.smc100.move(mc_index, position)
		
	def disconnect_hardware(self):
		''' disconnect from all hardware '''
		counted_file_writer.close_counted_file()
		self.dpc230.kill()
		self.smc100.kill()
		self.flipper.kill()
		
		
x=experiment()
# x.bayes.set_parameters(blah blah blah)
x.run_experiment()
x.disconnect_hardware()