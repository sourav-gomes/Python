# Use open function to read the contents of a file

f = open('/home/joseph/Downloads/python/Chapter 9 - File IO/sample.txt', 'r')
f = open('/home/joseph/Downloads/python/Chapter 9 - File IO/sample.txt')    # by default the mode is read i.e. 'r'

## Infact you can open a a file in 2 modes of read:
#  1) 'rt' which is equal to 'r' and 't' is by default, and resembles read in text mode
#  2) 'rb' which resembles read in binary mode eg. open('sample.txt', 'rb') for opening in binary mode
#  3) You need to explicitly specify 'rb' for reading in binary mode

# data = f.read()   # reads the full file
## You cannot read the contents of the file twice so you will have to comment out the first read

# data = f.read(6)   # will read the first 6 characters of the file
# print(data)
# f.close()

## Readline function:

# Reads the 1st line 
data1 = f.readline()
print(data1)
# prints gap of 1 line after every line because of the default /n 

# Reads the 2nd line 
data1 = f.readline()
print(data1)

# Reads the 3rd line 
data1 = f.readline()
print(data1)

# Reads the 4th line and so on... 
data1 = f.readline()
print(data1)

f.close()


