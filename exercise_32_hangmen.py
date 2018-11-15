"""


"""
print(__doc__)

import random

def var():
	global turn
	global guesslist
	user_input = str(raw_input("profide a letter: ")).upper()
	for counter in wordlen:
		if wordlist[counter] == user_input:
			guesslist[counter] = user_input
		print guesslist[counter],

	if user_input in guesslist:
		print ""
		score()
	else:
		turn = turn + 1
		print ""
		score()

def score():
	if turn > 5:
		print "you failed to guess the word %s mistakes where made" % (turn)
		exit()
	elif wordlist == guesslist:
		print "You made %s mistakes to guess the word" % (turn)
	else:
		var()

def hangman():
	print """| |__________))______|"""
	print """| | / /      ||       """
	print """| |/ /       ||       """
	print """| | /        ||*-''*      """
	print """| |/         |/  _  |     """
	print """| |          ||  |/||     """
	print """| |          (|||_||      """
	print """| |         *-|--'*       """
	print """| |        *Y | | Y*      """
	print """| |       ** |   | **     """
	print """| |      **  | | |  **    """
	print """| |     |)   |   |   (|   """
	print """| |          |||||        """
	print """| |          || ||        """
	print """| |          || ||        """
	print """| |          || ||        """
	print """| |         * | | *       """
	print """| |+++++++* *       |*|*| """
	print """| |        * *        | | """
	print """| |         * *       | | """
	print """| |          *|       | | """


turn = 0
wordlist = []
guess = ""

with open('wordlist.txt', 'r') as open_file:
	line = open_file.readline()
	while line:
		wordlist.append(str(line))
		line = open_file.readline()
number = random.randint(0,267751+1)
word = str(wordlist[number]).strip('\n')
wordlen = range(0,len(word))
wordlist = list(word)

for counter in wordlen:
	guess = guess + "_"
guesslist = list(guess)

if __name__=='__main__':
	hangman()
	var()


