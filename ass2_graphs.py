## ass2_graphs.py ######################################################
########################################################################


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

import math

def funcA(t):
	output = math.sin(220*np.pi*t) + 0.5*math.sin(440*np.pi*t)
	return output

def funcB(t):
	output = math.sin(220*np.pi*t) + 0.5*math.cos(440*np.pi*t)
	return output

if(__name__ == "__main__"):
	t_range = np.arange(0, 2.0*np.pi, 0.009)
	
	Avals = []
	Bvals = []
	
	for t in t_range:
		Avals.append(funcA(t))
		Bvals.append(funcB(t))		
	
	plt.title("plot from 0 to 2*pi")
	
	plt.plot(t_range, Avals, 'b', label="f = sin(220*pi*t) + 0.5*sin(440*pi*t)")
	plt.plot(t_range, Bvals, 'g', label="f = sin(220*pi*t) + 0.5*cos(440*pi*t)")
	
	plt.xlabel("t")
	plt.ylabel("f")		
	plt.legend()
	plt.savefig("ass2graph_full.png")

