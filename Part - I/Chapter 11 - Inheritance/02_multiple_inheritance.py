class Employer():
    company = 'Visa'
    empCode = 130

class Freelancer():
    company = 'Fiverr'
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employer, Freelancer):      # Note if company attribute is printed, then it will print 'Visa' as in the inheritance Employee is mentioned first, so priority will be given to Employee
    name = 'Rohit'

p = Programmer()

print(p.company)    #***IMP: Since it is multiple inheritance and both the base classes (Employer, Freelancer) has the attribiute 'company', so which one will it print???
# It will give priority to the attribute of the base class that has been mention first in the definition i.e. in this case class Programmer(Employer, Freelancer) => Employer. 
# So it will print 'Visa'

print(p.level)          # accessing & printing level value in Freelancer class. Output => 0 i.e. initial value

p.upgradeLevel()        # accessing upradeLevel() in the base class Freelancer

print(p.level)
