#!/usr/bin/python
'''

'''
import re
import sys
import numpy as np
from pylab import *
import shlex
import subprocess

args = "./a.out"
data=[]
handle=open(sys.argv[1], 'w')
for i in range(2000):
	p=subprocess.Popen(shlex.split(args),stdout=subprocess.PIPE)	#run the program
	temp=p.communicate()[0][:-1]	#grab the output and remove the last new line
	handle.write(temp)
	print(temp)
	data.append(float(temp))

plot(data,linewidth=1.0)
ylabel('time per mov (ns)')
xlabel('iterations')
title('average malloc times')
grid(True)
show()
handle.close()
