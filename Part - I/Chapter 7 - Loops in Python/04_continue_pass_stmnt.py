'''
# Continue statement will not execute that particular condition (say)

for i in range(10):
    if(i == 5):
        continue    # This will move to the next value of i i.e. 6 w/o printing 5 
    print(i)

# This can be used to print only odd nos for eg.

for i in range(100):
    if(i % 2) == 0:
        continue    # This will not print any nos which when divide by 2 gives 0 as remainder i.e. even nos 
    print(i)
'''

# Pass statement: It's a null statement. Instructs python to do nothing. 
# You can come back later and write code, so it will not throw an error

a = 3

if a>0:
    pass

while a>6:
    pass

print("Done")

# Same can be done with functions

def function1(a, b):    # This was function can be kept aside w/o throwing error and can come back later
    pass



