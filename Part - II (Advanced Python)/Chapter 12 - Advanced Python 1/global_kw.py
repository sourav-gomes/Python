global a 
a = 25      # assiging value to global variable

def func2():
    global a 
    print(f"func2() prints the value of GLOBAL variable a: {a+10}")     # re-assiging value to global variable

def func1():
    a = 50
    print(f"func1() prints the value of LOCAL variable a: {a}")

print(f"Printing Global variable before calling change function. a = {a}")
func1()
func2()