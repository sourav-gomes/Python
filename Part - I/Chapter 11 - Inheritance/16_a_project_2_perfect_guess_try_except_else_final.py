import random

randNo = random.randint(1, 100)
# print(randNo)

guesses = 0
usrGuess = None

while usrGuess != randNo:
    print("\nEnter 'q' to QUIT")
    usrGuess = input("Guess a number (1-100): ")

    if usrGuess == 'q':
        break
    
    try:
        usrGuess = int(usrGuess)

    except ValueError as e:
        print("You need to enter an integer value only. Eg. 12, 10, 5, etc.")
    
    else:
        guesses += 1

        if usrGuess == randNo:
            print(f"You guessed it correctly!")       
        else:
            if usrGuess > randNo:
                print("Sorry, wrong guess. The number is smaller. Try again...")
            else:
                print("Sorry, wrong guess. The number is bigger. Try again...")

# finally:
print(f"Number of guesses: {guesses}")

with open('hiscore.txt', 'r') as f:
    hiscore = int(f.read())

if guesses < hiscore:
    print("Congrats! You've just broken the highest score. Great going.")
    with open('hiscore.txt', 'w') as f:
        f.write(str(guesses)) 


