class Person():
    country = "India"

    def __init__(self):
        print(f"Initializing Person...")

    def takeBreath(self):
        print(f"I'm breathing...")

class Employee(Person):
    company = 'Microsoft'
    salary = 100

    def __init__(self):
        super().__init__()                  # will call the super class (i.e. Person) constructor
        print(f"Initializing Employee...")

    def takeBreath(self):
        super().takeBreath()
        print(f"I'm an Employee and I'm breathing...")

    def getSalary(self):
        print (f"Employee salary is ${self.salary}") 

class Freelancer(Employee):

    def __init__(self):
        # super().__init__()                  # will call the super class (i.e. Employee) constructor
        print(f"Initializing Freelancer...")
        
    def takeBreath(self):
        super().takeBreath()
        print(f"I'm a Freelancer and I'm breathing...")

    def getSalary(self):
        print (f"Hourly contract to Freelancers") 

p = Person()
p.takeBreath()      # Will print the takeBreath() of the class

e = Employee()
e.takeBreath()      # Will print the takeBreath() of the class and the super() will also print takeBreath() of the parent class

f = Freelancer()
f.takeBreath()      # Will print the takeBreath() of the class and the super() will also print takeBreath() of the parent class


p = Person()        # Will print the __init__() of the Person class
e = Employee()      # Will print the __init__() of the class and the super() will also print __init__() of the parent class
f = Freelancer()    # Will print the __init__() of the class and the super() will also print __init__() of the parent class