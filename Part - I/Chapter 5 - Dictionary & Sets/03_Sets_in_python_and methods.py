'''
a = (1, 2, 3)       # () means --> tuple
print(type(a))      # prints type --> <class 'tuple'>

a = [1, 2, 3]       # [] means --> list
print(type(a))      # prints type --> <class 'list'>

a = {1, 2, 3}       # {x, y,....} means --> set
print(type(a))      # prints type --> <class 'set'>

a = {1:3}           # {x:y} means --> dictionary
print(type(a))      # prints type --> <class 'dict'>

a = {}
print(type(a))      # Important this syntax will create an empty dictionary, NOT an empty set

# To create an empty set you use the following command

b = set()
print(type(b))

# Methods in Sets  

b.add(4)            # add() to add value to the set
b.add(10)

#  An object is hashable if it has a hash value that DOES NOT change during its entire lifetime

# b.add([1,3,6])      # cannot add a list to a set since a list is not hashable

# b.add((1,3,6))      # But you can add a tuple to a set

# b.add({5:8})      # cannot add a list to a set since a dictionar is not hashable

# Only HASHABLE datatypes can exist inside a set

print(b)

s = {1,4,4,1,6,1,6} 
print(s)            # will print only {1, 4, 6} since a set can have only unique values

print(len(s))       # prints length of set, in this case 3

s.remove(6)         # removes 6 from the above set of {1, 4, 6}
# s.remove(5)         # Throws error as 5 is not an element of the set above set of {1, 4, 6}
print(s)  

print(s.pop())      # Randomly removed a value from the set and returns the remaining

print(s.clear())    # Clears/Empties the set and returns None

'''

set1 = {2, 5, 6, 8}
set2 = {6, 3, 0, 1}

print(set1.union(set2))     # Eg. of set1 & set2 union

print(set1.intersection(set2))     # Eg. of set1 & set2 intersection (only 6 is common)
