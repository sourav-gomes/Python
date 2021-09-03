class Number:
    def __init__(self, num):        # contructor is also a dunder method
        self.num = num

    def __add__(self, num2):        # dunder method i.e. Double UNDERscore methods to override + operator
        print("Let's Add...", end="")
        return self.num + num2.num
    
    def __sub__(self, num2):        # dunder method i.e. Double UNDERscore methods to override - operator
        print("Let's Subtract...", end="")
        return self.num - num2.num
    
    def __mul__(self, num2):        # dunder method i.e. Double UNDERscore methods to override * operator
        print("Let's Multiply...", end="") 
        return self.num * num2.num
    
    def __truediv__(self, num2):    # dunder method i.e. Double UNDERscore methods to override / operator
        print("Let's Divide...", end="")
        return self.num / num2.num

    def __floordiv__(self, num2):    # dunder method i.e. Double UNDERscore methods to override / operator
        print("Let's Double slash...", end="")
        return self.num // num2.num
    
    # Other dunder methods
    def __str__(self):
        return f"Decimal No. : {self.num}"

    def __len__(self):
        return 1

n1 = Number(150)     # This is not an integer but a Number object

n2 = Number(100)     # This is not an integer but a Number object

sum = n1+n2
print(sum)

subtract = n1-n2
print(subtract)

multiply = n1*n2
print(multiply)

divide = n1/n2
print(divide)

doubleSlash = n1//n2        # double slashes divides but does not print the remainder or digits after . (point)
print(doubleSlash)

# Other dunder methods

print(n1)
print(len(n1))      # will execute the dunder method __len__() as above and will return 1 (say)
