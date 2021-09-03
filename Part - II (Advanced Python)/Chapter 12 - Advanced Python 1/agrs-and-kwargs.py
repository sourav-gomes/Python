# *agrs & **kwargs - Helps to take variable parameters
# But it's not mandatory to write *agrs & **kwargs ONLY * & ** is IMPORTANT
# For eg. You can also write *abc **xyz
#################
# SIMPLE EXAMPLE
#################
def function1(*args):
    print(type(args))   # will show that args is "TUPLE" (unchangeable) type variable
    print("Name is:", args[0], "Age is:", args[1], "Gender is:", args[2])

function1("Jose", 34, "Male")

#################
# MULTIPLE ARGUMENTS EXAMPLE
#################

def function2(*args):
    # print(type(args))   # will show that args is "TUPLE" (unchangeable) type variable
    if len(args) == 3:
        print("Name is:", args[0], "Age is:", args[1], "Gender is:", args[2])
    else:
        print("Name is:", args[0], "Age is:", args[1])

function2("Jose", 34, "Male")
function2("Hovsep", 42)

# Another Use case of *args
# Suppose I have a list|tuple and want to pass the values of list|tuple as argument

l1 = ["Jan", 54, "Female"]
l2 = ["Jake", 33]

function2(*l1)      # In case of list|tuple you need to add *<list|tuple_name>
function2(*l2)

## IMP: It's not important that to give *args, you can give *abc or *xyz or any.
## '*' is important. Writing the above using *xyz i place of *args

def function3(*xyz):
    # print(type(xyz))   # will show that args is "TUPLE" (unchangeable) type variable
    if len(xyz) == 3:
        print("Name is:", xyz[0], "Age is:", xyz[1], "Gender is:", xyz[2])
    else:
        print("Name is:", xyz[0], "Age is:", xyz[1])

function3(*l1)
function3(*l2)

#--------------------------------
# **KWARGS - Used for 'Dict' variable type with key-value pairs
#--------------------------------

def printmarks(**kwargs):
    print(type(kwargs))     # will show that args is "DICT" type variable
    for key, value in kwargs.items():   # .items is a fn() used for 'dict' type variables
        print(key,value)
        print("Name is:",key, "Marks is:", value)

marklist1 = {"Joseph": 90, "Sourav": 80, "Jan":98, "Jake": 55}
# Now even if we add any no. of name-marks key-value pair, and with kwargs it would just get added

printmarks(**marklist1)

## IMP: Similar to args It's not important that to give **kwargs, you can give **abc or **xyz or any.
## '**' is important. Will NOT show with example as it will be similar to *args

#----------------------------------
##  MIXING IT ALL -- Normal agrument + *args + **kwargs ALL TOGETHER
#----------------------------------

def master(normal_arg, *arg, **kwargs):
    print(normal_arg)

    for i in arg:
        print(i)
    
    for key, value in kwargs.items():
        print(key, value)

print("="*20)
master("Normal Argument", *l1, **marklist1)
print("="*20)


