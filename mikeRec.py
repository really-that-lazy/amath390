## mikeRec.py ##################################################################
## record input from microphone ################################################
################################################################################

## This is an example of a simple sound capture script.
##
## The script opens an ALSA pcm for sound capture. Set
## various attributes of the capture, and reads in a loop,
## Then prints the volume.
##
## To test it out, run it and shout at your microphone:

import alsaaudio, time, audioop

from sys import argv

import screwMatlab
import numpy as np


if(__name__ == "__main__"):
	outputFilename = argv[1]
	
	# Open the device in nonblocking capture mode. The last argument could
	# just as well have been zero for blocking mode. Then we could have
	# left out the sleep call in the bottom of the loop
	inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
	
	# Set attributes: Mono, 8000 Hz, 16 bit little endian samples
	inp.setchannels(1)
	inp.setrate(44100)
	inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
	
	# The period size controls the internal number of frames per period.
	# The significance of this parameter is documented in the ALSA api.
	# For our purposes, it is suficcient to know that reads from the device
	# will return this many frames. Each frame being 2 bytes long.
	# This means that the reads below will return either 320 bytes of data
	# or 0 bytes of data. The latter is possible because we are in nonblocking
	# mode.
	inp.setperiodsize(160)
	
	
	initTime = time.time()
	
	time_v = []
	data_v = []
	

	try:
		while (True):
			# Read data from device
			l,data = inp.read()
			if l:
				# Return the maximum of the absolute value of all samples in a fragment.
				print audioop.max(data, 2), (time.time() - initTime)
				time_v.append(time.time() - initTime)
				data_v.append(audioop.max(data, 2))
			time.sleep(.001)
	except KeyboardInterrupt:	
		screwMatlab.plotSpectrogram(np.array(time_v), np.array(data_v), outputFilename)
