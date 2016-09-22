## screwMatlab.py ##############################################################
## tryin ta spehctragram #######################################################
################################################################################

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy

import math

from scipy import signal

def plotSpectrogram(time, data, savefigTo='show'):
	print 'foo'
	NFFT = 200     # the length of the windowing segments
	Fs = 8000  # the sampling rate

	# plot signal and spectrogram

	ax1 = plt.subplot(211)
	plt.plot(time,data)   # for this one has to either undersample or zoom in 
	plt.xlim([0,max(time)])
	plt.subplot(212 )  # don't share the axis
	##Pxx, freqs, bins, im = plt.specgram(data, NFFT=NFFT,   Fs=Fs,noverlap=100, cmap=plt.cm.gist_heat)
	Pxx, freqs, bins, im = plt.specgram(data,noverlap=100, cmap=plt.cm.gist_heat)	
	if(savefigTo == 'show'):
		plt.show() 
	else:
		plt.savefig(savefigTo)

if(__name__ == "__main__"):
	time1 = np.arange(0,5,0.0001)
	time = np.arange(0,15,0.0001)
	
	##data1=np.sin(2*np.pi*300*time1)
	sig = np.sin(5000 * np.pi * time1)
	data1 = signal.square(time1, duty=(sig + 1)/2)	
	##data1 = signal.square(time1)
	print type(time1), data1
	print type(np.array([0,1,2,3,4]))
	
	data2=np.sin(2*np.pi*(900*(time1/max(time1)))*time1)
	##data2=np.array([math.sin((2*np.pi*(900+i)*i)) for i in time1])
	print time1/float(max(time1))
	
	data3=np.sin(2*np.pi*900*time1)
	
	data=np.append(data1,data2)
	data=np.append(data,data3)
	print len(time)
	print len(data)
	
	plotSpectrogram(time, data)
	plotSpectrogram(time, data, 'testfig.png')
