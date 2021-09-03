import random

randNo = random.randint(1, 100)
# print(randNo)

guesses = 0
usrGuess = None

while usrGuess != randNo:
    usrGuess = int(input("Guess a number (1-100): "))
    guesses += 1
    if usrGuess == randNo:
        print(f"You guessed it correctly!")       
    else:
        if usrGuess > randNo:
            print("Sorry, wrong guess. The number is smaller. Try again...")
        else:
            print("Sorry, wrong guess. The number is bigger. Try again...")

print(f"Number of guesses: {guesses}")

with open('hiscore.txt', 'r') as f:
    hiscore = int(f.read())

if guesses < hiscore:
    print("Congrats! You've just broken the highest score. Great going.")
    with open('hiscore.txt', 'w') as f:
        f.write(str(guesses)) 


