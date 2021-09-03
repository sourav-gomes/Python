
# My Logic - Working
'''
a1 = int(input("Enter a number1: "))
a2 = int(input("Enter a number2: "))
a3 = int(input("Enter a number3: "))
a4 = int(input("Enter a number4: "))

ag = 0

if(a1 > ag):
    ag = a1
if(a2 > ag):
    ag = a2
if(a3 > ag):
    ag = a3
if(a4 > ag):
    ag = a4

print("The greatest number is:", ag)
'''

# Harry's Logic

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
num3 = int(input("Enter a number3: "))
num4 = int(input("Enter a number4: "))

if(num1 > num2):
    f1 = num1
else:
    f1 = num2

if(num3 > num4):
    f2 = num3
else:
    f2 = num4

if(f1 > f2):
    print(str(f1) + " is the greatest")
else:
    print(str(f2) + " is the greatest")



