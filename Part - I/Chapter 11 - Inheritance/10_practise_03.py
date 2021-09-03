class Employee():
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, val):
        self.increment = val / self.salary      # Formula: incrementSalary = salary * increment

e = Employee()

print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 2500
print(e.increment)