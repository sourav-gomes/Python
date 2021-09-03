class Employee():
    company = "ABC"
    salary = 5600 
    salarybonus = 400
    # totalSalary = 5000      # Here we are hard coding total salary which is not desireable as the salary bonus may change

    # So to set properties internally and you need the getter & setter decorators

    @property               # The method name with property decorator is called the getter method
    def totalSalary(self):                  # will treat totalSalary like class property eg. salary or company
        return self.salary + self.salarybonus      # The getter/property function runs the f() to calculate the totalSalary
    
    @totalSalary.setter         # we can define a f() property.setter [here totalSalary] @totalSalary.setter decorator like below
    def totalSalary(self, val):
        self.salarybonus = val - self.salary        # changing the bonus amt as per value set

e = Employee()

print(e.totalSalary)        # Note: total.Salary though being a function is treated like class property which is calculated as variable
e.totalSalary = 5700        # This will trigger the @totalSalary.setter and the totalSalary(val), taking 5700 as the val
print(e.salary)
print(e.salarybonus)
