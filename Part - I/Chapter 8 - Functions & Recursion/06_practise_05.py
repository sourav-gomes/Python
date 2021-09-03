## Solution my way
'''
def pattern(n):
    for n in range(n, 0,-1):
        print("*" * n)

n = int(input("Input a number: "))

pattern(n)

'''

# Solution Harry's way

a = int(input("Input a number: "))

for i in range(a):
    print("*" * (a-i))      # Prints * n-i times i.e n-1
