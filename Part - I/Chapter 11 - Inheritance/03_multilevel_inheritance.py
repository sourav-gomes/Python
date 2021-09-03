class Person():
    country = "India"

    def takeBreath(self):
        print(f"I'm breathing...")

class Employee(Person):
    company = 'Microsoft'
    salary = 100

    def takeBreath(self):
        print(f"I'm an Employee and I'm breathing...")

    def getSalary(self):
        print (f"Employee salary is ${self.salary}") 

class Freelancer(Employee):
        
    def takeBreath(self):
        print(f"I'm a Freelancer and I'm breathing...")

    def getSalary(self):
        print (f"Hourly contract to Freelancers") 

p = Person()
print(p.country)
p.takeBreath()
# p.getSalary()       # Will throw error as there is no such f() in class Person

e = Employee()
print(e.country)    # Will print the value (India) for the parent class
print(e.company)    # Will print the value (India) for the parent class
e.takeBreath()      # Will print it's own method but if not present it will print the method of it's parent class (Person)
e.getSalary()       # Will print it's own method but if not present it will print the method of it's parent class (Person)

f = Freelancer()
print(e.company)    # Will print the value (India) for the parent class (Employee)
print(f.country)    # Will print the value (India) for the parent's parent class
f.takeBreath()      # Will print it's own method but if not present it will print the method of it's parent class (Employee)
f.getSalary()       # Will print it's own method but if not present it will print the method of it's parent class (Employee)
