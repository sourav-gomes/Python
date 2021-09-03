def game():
    return 88          # assuming the game is returning the score 246 (in this case)

score = game()          # assigning the returned value (score) to the variable

with open('hiscore.txt') as f:
    hiscoreStr = f.read()

if hiscoreStr == '':
    with open('hiscore.txt', 'w') as f:
             f.write(str(score))
else:
    with open('hiscore.txt') as f:      # opening file as read
        hiscore = int(f.read())         # 
        if hiscore < score:
            with open('hiscore.txt', 'w') as f:
                f.write(str(score))

