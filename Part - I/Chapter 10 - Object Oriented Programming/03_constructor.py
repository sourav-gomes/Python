class Employer:
    company = "Microsoft"
    def getSalary(self, sign):    # self is automatically passed. You can pass another 
        print(f"Salary is of the employee working at {self.company} is {self.salary}\n{sign}")  # passes signature 'B/R, Joseph'

    def __init__(self, nm, age, sex):       # Constructor to initialize objects
        self.nm = nm
        self.age = age
        self.sex = sex
        print("The object is created!")
    
    def getDetails(self):
        print(f"The name of the employee is {self.nm}")
        print(f"The age of the employee is {self.age}")
        print(f"The gender of the employee is {self.sex}")

    # @staticmethod           # You can by-pass the 'self' parameter declaration
    def greet(self):
        print(f"Hi! Good Morning {self.nm}")

obj1 = Employer('Joseph', 42, 'Male')

obj1.greet()

obj1.getDetails()