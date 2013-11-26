#!/usr/bin/python
import subprocess
import shlex
import re
import sys

baseName=sys.argv[1]
ntimes=int(sys.argv[2])
for j in range(10):
	print(j)
	handle=open(baseName+"_"+str(j),'ab')
	for i in range(ntimes):
		P=subprocess.Popen("./out",stdout=handle)

	
