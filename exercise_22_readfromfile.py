"""
Given a .txt file that has a list of a bunch of names, 
count how many of each name there are in the file, 
and print out the results to the screen
"""
print(__doc__)


def var():
	with open('names.txt', 'r') as open_file:
		line = open_file.readline()
		all_text = []
		while line:
			#print line
			all_text.append(str(line.strip()))
			line = open_file.readline()
		#all_text = open_file.read()
		
	dictionary = {}
	for name in all_text:
		if name in dictionary:
			score = dictionary[name] 
			score = score + 1
			dictionary[name] = score
		else:
			dictionary[name] = 1
	print dictionary






if __name__=='__main__':
	var()