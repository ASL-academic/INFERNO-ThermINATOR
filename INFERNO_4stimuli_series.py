#import the required modules
import RPi.GPIO as GPIO
import time
# set the pins numbering mode
GPIO.setmode(GPIO.BOARD)
# Select the GPIO pins used for the encoder K0-K3 data inputs
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
# Select the signal used to select ASK/FSK
GPIO.setup(18, GPIO.OUT)
# Select the signal used to enable/disable the modulator
GPIO.setup(22, GPIO.OUT)
# Disable the modulator by setting CE pin lo
GPIO.output (22, False)
# Set the modulator to ASK for On Off Keying 
# by setting MODSEL pin lo
GPIO.output (18, False)
# Initialise K0-K3 inputs of the encoder to 0000
GPIO.output (11, False)
GPIO.output (15, False)
GPIO.output (16, False)
GPIO.output (13, False)
# The On/Off code pairs correspond to the hand controller codes.
# True = '1', False ='0'
print "To clear the socket programming, press the green button"
print "for 5 seconds or more until the red light flashes slowly"
print "The socket is now in its learning mode and listening for"
print "a control code to be sent. It will accept the following" 
print "code pairs"
print "1011 and 0011 all ON and OFF"
print "1111 and 0111 socket1"
print "1110 and 0110 socket 2"
print "1101 and 0101 socket 3"
print "1100 and 0100 socket 4"
print "Hit CTL C for a clean exit"


try:

	################## 1 lamp here ##########################
		# 40 seconds of baseline (lamps off)
		time.sleep(40)

		# Turn socket 1/lamp 1 on		
		GPIO.output (13, True)
		GPIO.output (16, True)
		GPIO.output (15, True)
		GPIO.output (11, True)
		
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Leave lamp 1 on for 3.8 more seconds (4s total acute heat stimulation time)
		time.sleep(3.8)

		# Turn all lamps off
		GPIO.output (13, False)
		GPIO.output (16, False)
		GPIO.output (15, True)
		GPIO.output (11, True)
		
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Turn all lamps off (2nd signal, failsafe)
		GPIO.output (13, False)
		GPIO.output (16, False)
		GPIO.output (15, True)
		GPIO.output (11, True)
		
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Turn all lamps off (3rd signal, failsafe)
		GPIO.output (13, False)
		GPIO.output (16, False)
		GPIO.output (15, True)
		GPIO.output (11, True)
		
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Leave lamps off for 20 seconds (Interstimulus Interval)
		time.sleep(19.4)

	################## 2 lamps here ##########################
		# Turn socket 1/lamp 1 on
		GPIO.output (13, True)
		GPIO.output (16, True)
		GPIO.output (15, True)
		GPIO.output (11, True)
		
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Turn socket 2/lamp 2 on
		GPIO.output (13, True)
		GPIO.output (16, True)
		GPIO.output (15, True)
		GPIO.output (11, False)
		
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Leave the 2 lamps on for 3.6 more seconds (4s total acute heat stimulation time)
		time.sleep(3.6)

		# Turn all lamps off
		GPIO.output (13, False)
		GPIO.output (16, False)
		GPIO.output (15, True)
		GPIO.output (11, True)
		
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Turn all lamps off (2nd signal, failsafe)
		GPIO.output (13, False)
		GPIO.output (16, False)
		GPIO.output (15, True)
		GPIO.output (11, True)
		
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Turn all lamps off (3rd signal, failsafe)
		GPIO.output (13, False)
		GPIO.output (16, False)
		GPIO.output (15, True)
		GPIO.output (11, True)
		
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Leave lamps off for 20 seconds (Interstimulus Interval)
		time.sleep(19.4)

	################## 3 lamps here ##########################
		# Turn socket 1/lamp 1 on
		GPIO.output (13, True)
		GPIO.output (16, True)
		GPIO.output (15, True)
		GPIO.output (11, True)
	
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Turn socket 2/lamp 2 on
		GPIO.output (13, True)
		GPIO.output (16, True)
		GPIO.output (15, True)
		GPIO.output (11,  False)
	
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Turn socket 3/lamp 3 on
		GPIO.output (13, True)
		GPIO.output (16, True)
		GPIO.output (15, False)
		GPIO.output (11,  True)

		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Leave the 3 lamps on for 3.4 more seconds (4s total acute heat stimulation time)
		time.sleep(3.4)

		# Turn all lamps off
		GPIO.output (13, False)
		GPIO.output (16, False)
		GPIO.output (15, True)
		GPIO.output (11, True)
	
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Turn all lamps off (2nd signal, failsafe)
		GPIO.output (13, False)
		GPIO.output (16, False)
		GPIO.output (15, True)
		GPIO.output (11, True)	
		
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Turn all lamps off (3rd signal, failsafe)
		GPIO.output (13, False)
		GPIO.output (16, False)
		GPIO.output (15, True)
		GPIO.output (11, True)

		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.1)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.1)

		# Leave lamps off for 20 seconds (Interstimulus Interval)
		time.sleep(19.4)

	################## 4 lamps here ##########################
		# Turn all 4 sockets/lamps on
		GPIO.output (13, True)
		GPIO.output (16, False)
		GPIO.output (15, True)
		GPIO.output (11, True)

		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.2)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.2)

		# Leave the 3 lamps on for 3.4 more seconds (4s total acute heat stimulation time)
		time.sleep(3.6)

		# Turn all lamps off
		GPIO.output (13, False)
		GPIO.output (16, False)
		GPIO.output (15, True)
		GPIO.output (11, True)
		
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.2)
		# Disable the modulator
		GPIO.output (22, False)
		time.sleep(0.2)
		
		GPIO.cleanup()


except KeyboardInterrupt:
	GPIO.cleanup()