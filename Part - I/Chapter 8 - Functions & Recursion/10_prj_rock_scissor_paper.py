import random           # Import the random module

def game(comp, you):
    ## If 2 values a equal declare tie
    if comp == you:
        return None

    ## Checking all possibilities when computer chooses 'r'
    elif comp == 'r' and you == 's':
        return False
    elif comp == 'r' and you == 'p':
        return False

    ## Checking all possibilities when computer chooses 's'
    elif comp == 's' and you == 'p':
        return False
    elif comp == 's' and you == 'r':
        return True

    ## Checking all possibilities when computer chooses 'p'
    elif comp == 'p' and you == 'r':
        return True
    elif comp == 'p' and you == 's':
        return True
   
    
print("\nComputer Turn: Rock(r), Scissor(s) or Paper(p) :\n")

## Computer chooses Random no. b/w 1-3

randNo = random.randint(1, 3)

## Assigning 1, 2 or 3 chosen by computer randomly to r, s and p

if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 's'
elif randNo == 3:
    comp = 'p'

# Input your choice
you = input("Your Turn: Rock(r), Scissor(s) or Paper(p) :")

## Validate your input

if you == 'r' or you == 's' or you == 'p':
    a = game(comp, you)
else:
    print(f"\nYour input '{you}' is invalid. Try again...\n")
    exit()

## Printing the results

print(f"\nYou chose {you} and Computer chose {comp}\n")

if a == None:
    print(f"The game is a tie!\n")
elif a == True:
    print(f"You win!\n")
elif a == False:
    print(f"You lost!\n")