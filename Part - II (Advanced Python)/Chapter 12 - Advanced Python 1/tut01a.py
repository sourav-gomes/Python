# if(__name__ == "__main__")

import os

def impfunction():
    print("Joseph is a coder") 

def main():
    print(os.listdir("/"))
    print("This is a demo of __name__")

# ***NB: print(__name__) when executed from tut01a will print 'main' 
# But when executed from tut01b will print 'tut01a'
print(__name__)

# The if (__name__ == "__main__") statement will not run the code below this when imported and run from tut01b.py

if (__name__ == "__main__"):    # evaluates to name of the module. In this case main, but in tut01b is gives 'tut01a'

#     print(os.listdir("/"))
#     print("This is a demo of __name__")
    main()
