'''
greeting = "Good morning, "
name = input("Your Name: ")
print(greeting + name)        # string concatenation 2 strings using '+'
c = greeting + name         # string concatenation 2 strings and storing the value in variable
print(c, 'Have a good day')


# String Indexing

nm1 = "Joseph"
print(nm1[0], nm1[1], nm1[4])
# nm1[3] = "f"    --> NOT ALLOWED. You can access the index string but cannot change it like this

# Slicing

print(nm1[2:4])

print(nm1[:5])      # Automatically take the 1st index as begining of the string i.e 0 --> same as nm1[0:5]
print(nm1[0:])      # Automatically take the last index of the string i.e in this case 5 --> same as nm1[0:6]

# Negative Indexes

print(nm1[-1], nm1[-2])
print(nm1[0:-4], nm1[0:2])    # is the same is 0:2

'''
# Skip values 

name = "JosephIsGood"

print(name[0::2])       # will print every 2nd letter of the string starting from 0 (i.e. first), :: i.e. blank meaning till the end

print(name[3:8:3])       # will print every 3rd letter of the string starting from 3rd (i.e. e), :8: i.e. till 8th index (i.e. G) --> result - eI

print(name[len(name)::-1])