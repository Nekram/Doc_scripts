#!/usr/bin/python
'''
'''

import os, sys, re, shlex, subprocess
from time import sleep

# this function takes a 1-d list of numbers and makes a string out of it
def listToString(data):
	ret=""
	for i in data:
		ret+=str(i)+"\n"
	return ret

def getPSData(n,dom):
	command ="process-list "+dom
	data=[]
	for i in range(n+1):
		print(str(i) + "/"+str(n))		
		p = subprocess.Popen(shlex.split(command),stdout=subprocess.PIPE)
		temp=p.communicate()[0]
		temp=re.split('\n',temp)
		data.append(len(temp))
			
	return data

if __name__=='__main__':	
	data=getPSData(3000,sys.argv[1])
	handle=open(sys.argv[2],'w')
	handle.write(listToString(data))
	print("done!")		

