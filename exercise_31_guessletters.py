"""


"""
print(__doc__)

#imports


def var():
	global turn
	global guesslist
	user_input = raw_input("profide a letter: ")
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
	if wordlist == guesslist:
		print "You made %s mistakes to guess the word" % (turn)
	else:
		var()


turn = 0
word = "evaporate"
wordlen = range(0,len(word))
wordlist = list(word)

guess = ""
for counter in wordlen:
	guess = guess + "_"
guesslist = list(guess)


if __name__=='__main__':
	var()
	
