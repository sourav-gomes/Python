a = input('Enter your name: ')
b = input('Enter your age: ')
print(type(b))      # input() takes every input as string. You then need to convert it to integer or float with type casting
b = float(b)        # converting age to float
print("Your name is ", a, "and your age is", b)