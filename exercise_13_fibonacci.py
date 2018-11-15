def fibonacci():
	number = int(raw_input("How many fibonacci numbers do you want to generate?"))
	
	#we start with 2 fibonacci numbers so we have a basis to work with in our loop
	fibonaccilist = [1, 1]
	#since we start with 2 fibonacci numbers we have to check if the number 2 is filled in by the user.
	if number == 2:
		print fibonaccilist
	#if the number is 1 we return one fibonacci number
	elif number == 1:
		print [1]
	#if its lower then 0 we can't return a fibonacci number and we ask the user to profide a bigger number
	elif number <= 0:
		print "Please profide a number bigger than 0"
		fibonacci()
	#else we start creating our fibonacci list
	else:
		#we allready have 2 fibonacci numbers in our list so we adjust our range.
		looper = range(0, number - 2)
		#we now loop over the range to create our fibonacci list
		for x in looper:
			add = fibonaccilist[x] + fibonaccilist[x +1]
			fibonaccilist.append(add)
		print fibonaccilist
			

fibonacci()