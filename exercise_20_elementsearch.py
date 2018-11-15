"""
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) 
and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

"""
print(__doc__)




def search(a,b):
	if b in a:
		return True
	else:
		return False


a = [1,2,3,4,5,6,7,8,9]
b = 1

if __name__=='__main__':
	print search(a,b)
	print search(a,2)
	print search(a,10)


	#replace("\n", " ")