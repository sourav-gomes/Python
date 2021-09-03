class Animal:
    type = "Mammal"

class Pet(Animal):
    color = "Brown"

class Dog(Pet):
    
    @staticmethod
    def bark():
        print (f"Bow! Bow!")

d = Dog()
d.bark()
print(d.type)
print(d.color)