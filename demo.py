#!/usr/bin/python3

import math
import time
import random

colours = [
	"\033[0;34m",
	"\033[0;32m",
	"\033[0;36m",
	"\033[0;31m",
	"\033[0;35m",
	"\033[0;33m",
	"\033[1;34m",
	"\033[1;32m",
	"\033[1;36m",
	"\033[1;31m",
	"\033[1;35m",
	"\033[1;33m"
]

bg_c = [
	"\u001b[40m",
	"\u001b[41m",
	"\u001b[42m",
	"\u001b[43m",
	"\u001b[44m",
	"\u001b[45m",
	"\u001b[46m",
	"\u001b[47m",
	"\u001b[40;1m",
	"\u001b[41;1m",
	"\u001b[42;1m",
	"\u001b[43;1m",
	"\u001b[44;1m",
	"\u001b[45;1m",
	"\u001b[46;1m",
	"\u001b[47;1m",
]

clear = "\033[0m"

def fg ():
	return colours[random.randint(0,11)]

def bg ():
	return bg_c[random.randint(0,15)]

i = 0
while True:
	spaces = int(math.sin(i*0.1)*50)+100
	print (bg()," "*spaces,fg(),bg(),spaces,bg())
	i += 1
	time.sleep(.150)