#File input / Output
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()

#lesson 1
my_file = open("output.txt", "r+")

#lesson 2
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!
for i in my_list:
  my_file.write(str(i) +"\n")
my_file.close()

#lesson 3
my_file = open("output.txt", "r")
#w for write
#r for read
#r+ for read and write
#a for append (write data to the end of the file)
print my_file.read()
my_file.close()

#lesson 4
my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()


#lesson 5 closing files
# Use a file handler to open a file for writing
write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()


# Try to read from the file
print read_file.read()
read_file.close()

#lesson 6
with open("text.txt", "w") as textfile:
  textfile.write("Success!")


#lesson 7
my_list = [i ** 2 for i in range(1, 11)]
print my_list
with open("text.txt", "w") as my_file:
  for i in my_list:
    my_file.write(str(i) + "\n")

with open("text.txt", "r") as my_file:
  print my_file.read()