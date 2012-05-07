#!/usr/bin/python
'''
	makePupPlot.py 
	This program graphs our results of the length of the ps result. 
	
	brandon marken 2012 (c)
	brandon.marken@gmail.com	
'''

import sys, re
import matplotlib.pyplot as plt
fname=sys.argv[1]
handle=open(fname,'r')
data=[]
for line in handle:
	data.append(int(line))

plt.plot(data)
plt.show()

