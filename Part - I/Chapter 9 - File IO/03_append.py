# Append to a file  
'''
f = open('another.txt', 'a')        # Use 'a' to append & it will append at the end of the file
f.write('Please write this to the file... AGAIN')
f.close()

# with ... as command --> You don't have to explicitly close() file

with open('another.txt', 'r') as f:     # opens in read mode
    a = f.read()
    print(a)

with open('another.txt', 'w') as f:     # opens in write mode
    a = f.write("with... write()... will replace content ")

with open('another.txt', 'a') as f:     # opens in append mode
    a = f.write("will append to the content")

'''

# Using the r+ mode 

f = open('sample.txt', 'r+')        # Use '+' to both read & write
a = f.read()
print(a)
f.write('using the plus mode\n')
f.close()
