class Employer:
    company = "Microsoft"
    def getSalary(self, sign):    # self is automatically passed. You can pass another 
        print(f"Salary is of the employee working at {self.company} is {self.salary}\n{sign}")  # passes signature 'B/R, Joseph'

    @staticmethod           # You can by-pass the 'self' parameter declaration
    def greet(nm):
        print(f"Hi! Good Morning {nm}")


joe = Employer()
joe.salary = 10000

joe.getSalary("B/R, Joseph")    # this line translates to ==>  Employer.getSalary(joe). 
# So the getSalary(self), self translates to the object/instance joe in Employer.getSalary(joe)
# This helps you to access all the other Object & class attributes in the class Employer as self.company

# Instance attributes take preference over class attributes during assignment & retrieval

joe.greet("Joe")     # this line translates to ==>  Employer.greet() because of @staticmethod declaration to bypass the 'self' parameter