class Employer:             # base or parent class
    company = 'Google'
    
    def showDetails(self):
        print("This is an employee (from parent class)")
    
    def test(self):
        print("Will inherit this from the base (Employer) class")

class Programmer(Employer):     # derived or child class of Employer
    language = 'Python'
    # company = 'YouTube'         # p.company will override the value of e.company and print Youtube. Without this p.company will display => Google

    def showDetails(self):      # Overriding Base class (Employer) showDetails()
        print("This is a programmer (from child class)")

    def showLanguage(self):
        print(f"The language is: {self.language} (Added f() in child class)")

e = Employer()
p = Programmer()

print(e.company)    # will print Google
print(p.company)    # will print Google if you don't override. If you dont override then it will print 'YouTube'

p.test()     # Will inherit this from the base (Employer) class, though this f() is not defined in the Programmer class
p.showDetails()   
p.showLanguage()