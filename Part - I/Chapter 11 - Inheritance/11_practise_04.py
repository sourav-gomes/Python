class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return Complex(self.real + c.real, self.imaginary + c.imaginary)    
        # ***IMP:the __add__() dunder method returns an object of the same class Complex from within itself

    def __mul__(self, c):
        # Complex No. formula to be used: (a+bi)(c+di) = (ac-bd)+(ad+bc)i
        mulReal = (self.real * c.real) - (self.imaginary*c.imaginary)   # (ac-bd)
        mulImg = (self.real * c.imaginary) + (self.imaginary*c.real)    # (ad+bc)
        return Complex(mulReal, mulImg) 

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(3, 2)
c2 = Complex(1, 7)

sum = c1 + c2
print(sum)

mul = c1 * c2
print(mul)