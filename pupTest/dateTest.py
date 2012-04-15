#!/usr/bin/python
'''

'''
import os, sys, re, shlex, subprocess
import datetime

'''
	monToNum function
	takes a string mon 
'''
def monToNum(mon):
	if mon=="Jan":
		return 1
	elif mon=="Feb":
		return 2
	elif mon=="Mar":
		return 3
	elif mon=="Apr":
		return 4
	elif mon=="May":
		return 5
	elif mon=="Jun":
		return 6
	elif mon=="Jul":
		return 7
	elif mon=="Aug":
		return 8
	elif mon=="Sep":
		return 9
	elif mon=="Oct":
		return 10
	elif mon=="Nov":
		return 11
	elif mon=="Dec":
		return 12

'''
	parseTime function
	takes in the output of vt-date and returns a datetime object
'''
def parseTime(vixTime):
	#removes the vix data
	time=re.split("\n",vixTime)
	time=time[2]
	
	#splits the date up by spaces
	time=re.split(" ",time)	

	#splits the time away from the data 
	clockTime=time[3]
	clockTime=re.split(":",clockTime)
	result=datetime.datetime(int(time[4]),int(monToNum(time[1])),int(clockTime[0]),int(clockTime[1]),int(clockTime[2]))
	return result

def getData(n,dom,kernel):
	command = "/home/brandon/Projects/vix/vix-tl/cli-utils/linux/bin"
	command +="/vt-date -d "+ dom+" -k "+kernel
	data=[]

	for i in range(int(n)+1):
		p = subprocess.Popen(shlex.split(command),stdout=subprocess.PIPE)
		temp=p.communicate()[0]
		temp=parseTime(temp)
		data.append(temp)
	return data

'''
	The getDeltas function
	takes a list and returns another list of the time delta
'''
def getDeltas(data):
	delta=[]
	for i in range(len(data)-1):
		delta.append(data[i+1]-data[i])
	return delta

def main():
	n=sys.argv[1]
	dom=sys.argv[2]
	kernel=sys.argv[3]
	data=getData(n,dom,kernel)
	print(data)
	#print(getDeltas(data))

if __name__=='__main__':
	main()
