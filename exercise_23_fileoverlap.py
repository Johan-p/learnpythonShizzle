"""
Given two .txt files that have lists of numbers in them, 
find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, 
and the other .txt file has a list of happy numbers up to 1000.
"""
print(__doc__)


def var():
	overlap = []
	prime = []
	happieslist = []

	with open('prime.txt', 'r') as open_file:
		line = open_file.readline()
		all_text = []
		while line:
			#print line
			prime.append(int(line))
			line = open_file.readline()
	
	with open('happies.txt', 'r') as open_file:
		line = open_file.readline()
		while line:
			#print line
			happieslist.append(int(line))
			line = open_file.readline()

	for x in prime:
		if x in happieslist:
			overlap.append(x)
	print overlap



if __name__=='__main__':
	var()