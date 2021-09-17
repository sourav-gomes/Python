from functools import reduce
l1 = [4,65,76,23,98]

## MY SOLUTION - where I define a lambda maxList fn() 

maxList = lambda a,b: a if a>b  else b      # My own max fn(). Will return a if a>b else it will return b as max b/w a & b

maxNum = reduce(maxList, l1)

print(maxNum)

## HARRY's SOLUTION - using the inbuilt max fn() of Python

a = reduce(max,l1)      # using Python in-built max(). Output - same

print(a)


