#************************************************************
# Procedural Oriented Programing (Normal way of programing that we have been doing till now i.e. this chapter)
#************************************************************
'''
a = 12
b = 20
print('The sum of a+b is:', a+b)
'''
#************************************************************
# Now the same above in oops i.e. Object oriented programming
#************************************************************
# Pascal case eg.:  PascalCase, EmployeeName etc.
# Classes are generally written in PascalCase
# Camel case eg.:  isNumeric, isFloatOrInt, camelCase etc.
# Class is like a template eg. Railway Form
# Object - is an instantiation of a class. Eg. when you fill up the Railway Form
# ***IMP: Memory is defined ONLY after object instantiation

class Number:               # defining a class
    def sum(self):          # defining function inside a class
        return self.a + self.b

num = Number()      # object instantiation

num.a = 12
num.b = 20

s = num.sum()

print(s)


#**************************************************************
# Modelling a problem in Oops i.e. Object oriented programming
#**************************************************************

# Name          ==> Class       ==> eg. Employee   
# Adjectives    ==> Attributes  ==> eg. name, age, sex, salary, etc.
# Verbs         ==> Methods     ==> eg. getSalary(), increment(), etc.

# Displaying class attributes

class Employee:
    company = 'Google'      # class attribute
    salary = '100k'

joe = Employee()        # Object instantiation
sam = Employee()        # Object instantiation

print(joe.company)      # Prints class attribute
print(sam.company)      # Prints class attribute

Employee.company = 'YouTube'    # Changing class trribute

print(joe.company)      # Prints changed class attribute
print(sam.company)      # Prints changed class attribute

joe.salary = '30k'      # Here salary is an Instance attribute

#**************************************************************
# While printing attribute it will... 
# 1) First check if there is any Instance/object attribute. If there is, it wil print obj/inst attribute, In this case for joe.salary it will print 30k
# 2) Second it will check class attribute. If present it will print that. For eg. in case of sam.salary it will print 100k
# 3) If it doesn't find the Instance or class attribute, it will throw error
#**************************************************************

print(joe.salary)      # Prints instance/object attribute ==> will print 30k
print(sam.salary)      # Prints class attribute ==> will print 100k
# print(joe.increment)   # Will throw error as the attribute increment is not present in Instance or class




