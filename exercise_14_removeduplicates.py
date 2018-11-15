a = [1,1,5,6,8,9,9,10]

def removeduplicates():
	b = []
	for num in a:
		if num not in b:
			b.append(num)
	return b

removeduplicates()


#solution 2 with set
def removedupes2(number):
	return list(set(number))

print a
print removeduplicates()
print removedupes2(a)
