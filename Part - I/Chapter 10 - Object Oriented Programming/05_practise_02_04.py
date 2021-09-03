# Problem #2: Write a program to calculate square, cube & square root
# Solution -->> My way
'''
import math

class Calculator:
    def __init__(self, num):
        self.num = num

    def calculate(self):
        square = self.num ** 2
        cube = self.num ** 3
        sqroot = math.sqrt(self.num)
        print(f"The square of {self.num} is: {square}")
        print(f"The cube of {self.num} is: {cube}")
        print(f"The square root of {self.num} is: {sqroot}")


number = int((input("Enter a number: ")))
num = Calculator(number)

num.calculate()

'''

# Problem #2: Write a program to calculate square, cube & square root
# Solution -->> Harry's way

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        square = self.num ** 2
        print(f"The square of {self.num} is: {square}")
        
    def cube(self):
        cube = self.num ** 3
        print(f"The cube of {self.num} is: {cube}")

    def sqroot(self):
        sqroot = self.num ** 0.5
        print(f"The square root of {self.num} is: {sqroot}")
    
    # This static greet() is the requirement for problem #4
    @staticmethod
    def greet():
        print("Hello!")


number = int((input("Enter a number: ")))
num = Calculator(number)
num.greet()
num.square()
num.cube()
num.sqroot()
