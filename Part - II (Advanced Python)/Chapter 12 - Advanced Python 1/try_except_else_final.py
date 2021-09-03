# ****************************
# Example #1
# ****************************
# open("this.txt")    # Without try command will give error and stop executing the program further
# print("The program WILL STOP and NOT display this line after printing the error msg")
# Output: FileNotFoundError: [Errno 2] No such file or directory: 'this.txt'
# The error is beacuse it cannot find the file 'this.txt' in the folder
'''
try:        # mean first it will try to run this code in the try block > open("this.txt"). If it cannot then it will run the code in the exception block
    open("this.txt")
except Exception as e:  # This will capture the error and display|print as a msg to usr
    print(e)
print("The program won't stop but display this line after printing exception error msg")
# Output:
# [Errno 2] No such file or directory: 'this.txt'
# The program won't stop but display this line after printing exception error msg

# ****************************
# EXAMPLE #2 :  HANDLING MULTIPLE EXCEPTIONS
# ****************************

try:
    file = open('this.txt', 'r')

except EOFError as e:
    print("EOF Error")  # Remember we can do a host of things under this block, as a result of the occurence. Here we are only executing a print command
except FileNotFoundError as e:
    print("FileNotFound Error")  # Remember we can do a host of things under this block, as a result of the occurence. Here we are only executing a print command

finally:
    print("This command or block of commands will get executed irrespective if there's any exception or not")

# ****************************
# EXAMPLE #3 :  SQUARING A NUMBER with try... exception... else.. finally
# ****************************
while(True):

    print("Enter 'q' to QUIT")
    a = input("Enter a Number: ")
    
    if a == 'q':
        break
    
    try:
        a = int(a)

    except ValueError as e:
        print("You need to enter an integer value only. Eg. 12, 10, 5, etc.")

    else:       # This code will run only if there's NO exception
        print(f"The SQUARE of the Number is: {a*a}")

    finally:    # The code here will run irrespective if there's an error or not
        print("Thank You for playing this game!\n")

'''

# ****************************
# EXAMPLE #4 :  RAISE ERROR with try... exception... 
# ****************************

def increment1(num):
    try:
        return int(num)+1
    except:
        raise ValueError("Please input an integer")

print(increment1(55))    # should produce output of 56

print(increment1('ty66'))    # should RAISE The exception ValueError 