class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getinfo(self):
        print(f"The name of the {self.company} employee is {self.name} and the product is {self.product}")

joe = Programmer('Joe', 'Skype')
sam = Programmer('Sam', 'GitHub')

joe.getinfo()
sam.getinfo()