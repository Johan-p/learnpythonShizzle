'''
The program should do the following:
Prompt the user to select a shape.
Calculate the area of that shape.
Print the area of that shape to the user.
'''
print "calculator is starting up"
name = raw_input("Enter C for Circle or T for Triangle: ")

if name == 'C':
  radius = float(raw_input("Enter radius: "))
  area = 3.14159 * radius**2
  print "The area of the Circle is %s" % (area)
  
elif name == 'T':
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = 0.5 * base * height
  print "The Area of the Triangle is %s" % (area)

else:
  print "You have entered an invalid shape."
  
print "exiting program"