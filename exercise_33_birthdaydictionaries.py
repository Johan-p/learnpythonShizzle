"""
or this exercise, we will keep track of when our friends birthdays are,
and be able to find that information based on their name. 
Create a dictionary (in your file) of names and birthdays. 
When you run your program it should ask the user to enter a name, 
and return the birthday of that person back to them. 
"""
print(__doc__)

#imports


def var():
	pass


birthday_dictionary = {"Albert Einstein":"14/03/1879",
                       "Benjamin Franklin":"17/01/1706",
                       "Winston Churchill":"24/01/1965",}

if __name__=='__main__':
	print "Welcome to the birthday dictionary. We know the birthdays of:"
	for key in birthday_dictionary.keys():
		print key
	user_input = str(raw_input("Who's birthday do you want to look up? "))
	if user_input in birthday_dictionary:
		print "%s birthday is %s" % (user_input, birthday_dictionary[user_input])
	else:
		exit()