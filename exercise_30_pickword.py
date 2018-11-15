"""
Given two .txt files that have lists of numbers in them, 
find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, 
and the other .txt file has a list of happy numbers up to 1000.
"""
print(__doc__)

import random

def var():
	wordlist = []
	with open('wordlist.txt', 'r') as open_file:
		line = open_file.readline()
		while line:
			wordlist.append(str(line))
			line = open_file.readline()
	number = random.randint(0,267751+1)
	print wordlist[number]

if __name__=='__main__':
	var()