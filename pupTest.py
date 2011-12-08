#!/usr/bin/python
'''
'''

import os, sys, re, shlex, subprocess

def main():
	command = "/home/brandon/Projects/vix-new-brandon/vix-tl/cli-utils/linux/bin"
	command +="/vt-ps -d 1 -k 2.6.32-686"
	p = subprocess.Popen(shlex.split(command))
	print(p) 

if __name__=='__main__':
	main()
