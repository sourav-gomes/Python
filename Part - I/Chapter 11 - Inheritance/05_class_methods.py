class Employee():
    company = "ABC"
    salary = 100        # This is a class attribute not instance attribute
    '''
    # Method #1: To change the class attribute:
    def changeSalary(self, sal):
        self.salary = sal   # Note: This will create a new instance attribute, 'salary' and assign the value 'sal' passed
        print(Employee.salary)      # Class attribute 'salary' will not change
        self.__class__.salary = sal     # Note: This will change the class attribute, 'salary' and assign the value 'sal' passed
        print(Employee.salary)
    ''' 
    # Method #2 (Recommended): To change the class attribute:
    @classmethod                        # this is a classmethod decorator
    def changeSalary(cls, sal):         # You can give more arguments eg. sal, company etc.
        cls.salary = sal   # Note: cls.salary will change the class attribute, 'salary' and assign the value 'sal' passed
        print(Employee.salary) 

e = Employee()
e.changeSalary(10000)