import sys
import numpy as np
import math

def count(n):
	if n>=1:
		a = 1
		b = 2
		
		for i in range(2, n+1):
			c = a+b
			a = b
			b = c

		BitString = b % math.pow(10,15)

		print(str(n) + "\t" + str(BitString))
	else:
		print(str(n) + "\tconstrain voilated")

files = sys.argv

InputFile = open(files[1],'r')
line = InputFile.readline()
line = InputFile.readline()

while line:
	if line.strip():
		count(int(line.strip()))
	line = InputFile.readline()

InputFile.close()
