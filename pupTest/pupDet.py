#!/usr/bin/python
from datetime import datetime
import os, sys, re, shlex, subprocess

def isMon(taul,taum):
	handle=open("results",'w')
	while True:
		t1=datetime.now()
		t2=datetime.now()
		if (t2-t1>0.01) and (t2-t1>taum):
			res=str(t1)+" "+str(t2)+"monitored"
			handle.write(res)
		else:
			res=str(t1)+" "+str(t2)+"unmonitored"
			handle.write(res)


if __name__=='__main__':
	isMon(0.1,1)	
