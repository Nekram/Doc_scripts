#!/usr/bin/python
'''
'''

import os, sys, re, shlex, subprocess



def getPSData(n,dom,kernel):
	command = "/home/brandon/Projects/vix/vix-tl/cli-utils/linux/bin"
	command +="/vt-ps -d "+ dom" -k "+kernel
	data=[]
	p = subprocess.Popen(shlex.split(command),stdout=subprocess.PIPE)
	for i in range(n+1):
		temp=len(p.communicate()[0])
		data.append(temp)
	return temp

def main():
	p = subprocess.Popen(shlex.split(command))
	print(p) 

