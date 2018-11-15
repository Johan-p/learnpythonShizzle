def exercise():
	name = raw_input("What's your name?")
	age = raw_input("How old are you?")
	when_100 = 100 - int(age)
	print "%s You will turn 100 years in %s years" % (name, when_100)

exercise()

