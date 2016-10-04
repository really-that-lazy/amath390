

import numpy as np
import math

def lengthByParams(f, T, rho, A):
	output = 1/(2.0*f)
	output *= math.sqrt(T/(rho*A))
	return output

def aByParams(f, T, rho, l):
	output = T
	output /= (4.0*rho*((f**2)*(l**2)))
	return output


def dByArea(A):
	output = 2.0*math.sqrt(A/np.pi)
	return output

if(__name__ == "__main__"):
	a = (np.pi*(0.00075**2))
	print a
	print lengthByParams(33, 239.31, 7860.0, a)

	newA = aByParams(33, 239.31, 7860.0, 0.501)
	
	print newA
	
	print dByArea(newA)
