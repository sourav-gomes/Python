# Tuples --> Main diff b/w Lists & Tuples is that you cannot update Tuples

t=(7,2,5,2,88,0)

print(t)
print(t[4])     # will print the 4th index element

# t[1] = 33       # will thow ERROR as couple values cannot be changed
# print(t)

t1 = ()     # declares empty tuple
print(t1)

t2 = (1)    # WRONG way of declaring tuple with 1 element. Interpreter does not understand it's a tuple. It takes as an integer
print(t2)

t3 = (55,)    # Right way of declaring tuple with single element
print(t3)

