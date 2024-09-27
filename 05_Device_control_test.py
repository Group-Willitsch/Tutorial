######################################################
#                                                    #
#                DEVICE    CONTROL                   #
#                      TEST                          #
#                 REIN Experiment                    #
#                                                    #
######################################################
# Adrien Poindron, Sep. 2024.
#
# Program to test the connection to instruments
# And their control through pyvisa.

import pyvisa
from pyvisa.constants import StopBits, Parity

class InstrumentManager:
	'''
	Class to open and close connection with instruments using pyvisa.
	It is also setting the internal parameters of the devices.
	'''
	def __init__(self):
		self.AWG_address  = 'USB::0x05E6::0x3390::8011219::INSTR'
		self.AFG_address  = 'USB::0x0699::0x0353::1650326::INSTR'
		self.TAC_address  = 'ASRL8::INSTR'
		self.DSP_address  = 'ASRL7::INSTR'
		self.FAG_address  = 'USB0::0x1AB1::0x0642::DG1ZA254205102::INSTR'

	# Connecting to devices
	def connect_to_devices(self):
		'''
		Uses the resource manager to discover the instruments connected
		to the computer and open the resources. The correct ID must be
		entered, the line 'print(rm.list_resources())' is showing all
		the addresses of the visible devices. Here AWG is an AFG
		and TAC is the SR620 TAC.
		'''
		rm = pyvisa.ResourceManager()
		print(rm.list_resources())
		print()

		## Connecting to AwG Keithley
		# RF supply
		AWG = rm.open_resource(self.AWG_address) # AWG
		print("AWG 3390 wave function generator connected with pyvisa.")
		print(AWG)
		AWG.write('*IDN?')
		print(AWG.read())

		## Connecting to AFG
		# Tickle and NanoWire drive
		AFG = rm.open_resource(self.AFG_address) # AWG
		
		print("AFG 1062 wave function generator connected with pyvisa.")
		print(AFG)
		AFG.write('*IDN?')
		print(AFG.read())

		## Connecting to DSP
		# Compensation voltage
		DSP = rm.open_resource(self.DSP_address,
							baud_rate = 115200,
							data_bits = 8,
							stop_bits = StopBits.one,
							parity    = Parity.none)
		
		print("DSP-3005 DC power supply connected with pyvisa.")
		print(DSP)
		DSP.write('*IDN?')
		print(DSP.read())

        ## Connecting to FAG
        # Frequency reference for counter
		FAG = rm.open_resource(self.FAG_address)
		
		print("DG1022Z Function/Arbitrary Generator connected with pyvisa.")
		print(FAG)
		FAG.write('*IDN?')
		print(FAG.read())

		## Connecting to counter
		TAC = rm.open_resource(self.TAC_address,
							baud_rate = 19200,
							data_bits = 8,
							stop_bits = StopBits(20),
							parity    = Parity(0)) #connect to the TAC (Stanford Research Systems SR620)
		print("SR620 Time to Amplitude Converter connected with pyvisa.")
		print(TAC)
		TAC.write('*IDN?')
		print(TAC.read())
		
		print('')

		return AWG, AFG, DSP, FAG, TAC
	
	def close_connection(self, AWG, AFG, DSP, FAG, TAC):
		'''
		Closes connection with instruments.
		'''	
		AWG.close()
		AFG.close()
		DSP.close()
		FAG.close()
		TAC.close()
				
	def set_DSP(self, DSP, Voltage, Output):
		print('=========')
		# DSP.write(f"SYSTem:REMote")
		DSP.write(f"OUTPut {Output}")
		DSP.write(f"VOLTage {Voltage}")
		DSP.write('MEASure:ALL:INFO?')
		print(DSP.read())

	def set_FAG(self, FAG, Waveform, Voltage, Frequency, Output):
		print('=========')
		# DSP.write(f"SYSTem:REMote")
		FAG.write(f"OUTPut {Output}")
		FAG.write(f"VOLTage {Voltage}")
		FAG.write(f'FUNCtion {Waveform}')
		FAG.write(f'FREQuency {Frequency}')
		print(FAG.read())
		
# MAIN PROGRAM
Instruments = InstrumentManager()

AWG, AFG, DSP, FAG, TAC = Instruments.connect_to_devices()
Instruments.set_DSP(DSP, 1, 1)
Instruments.set_FAG(FAG, 'SIN', 5, 422500, 'ON')
Instruments.close_connection(AWG, AFG, DSP, FAG, TAC)