#!/usr/bin/python
import re
import sys
import numpy as np
from pylab import *

handle = open(sys.argv[1],'r')
line=handle.read()
line=re.split('\n',line)
line=line[:-1]					#pop off that last new line
data=[]
for i in line:
	data.append(float(i)*100) #convert to nano seconds

plot(data,linewidth=1.0)
ylabel('time per malloc (ns)')
title('average malloc times')
grid(True)
show()
