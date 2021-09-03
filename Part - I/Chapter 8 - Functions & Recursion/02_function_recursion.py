## Recursion: Calling a function from within itself. Generally used in factorials.
'''
import sys          # importing sys to reset recursion limit

sys.getrecursionlimit()
# sys.setrecursionlimit(2000)     

i = 1

def greet():
    global i
    print("Hi!", i)
    i += 1
    greet()         # calling greet from within itself. Will create an infinite loop. However in Python it's limited to 1000 (which can be increased. Refer the serRecursionlimit above)

greet()     # calling greet from outside

'''

# Check by defining factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(9)
# print(factorial(9))
print(f)