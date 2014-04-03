#!/usr/bin/python
'''
'''

import os, sys, re, shlex, subprocess
from time import sleep

while True:
	p = subprocess.Popen(shlex.split("process-list Crace"),stdout=subprocess.PIPE)
	temp=p.communicate()[0]
			


