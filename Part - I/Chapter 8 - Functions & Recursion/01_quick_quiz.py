def hi():
    print("Hi")

def greet(name = "Stranger"):       # passing default argument i.e. name = "Stranger"
    p = print("Hello!", name)
    return p

def getSum(num1, num2):
    return num1+num2

hi()

greet("Jack")

greet()         # Accessing default Argument "Stranger" when we don't pass any argument

a = getSum(40, 60)
print(a)


