story = "once upon a time there was a boy named Joseph who was good but very lazy fellow and never completed any job"

# String Functions

# print(len(story))       # gives length of the string
# print(story.endswith("job"))    # returns True or false. In this case True.
# print(story.count("a"))    # returns how many times a character 'a' has occurred
# print(story.count("was"))    # returns how many times a string 'was' has occurred, in this case 2
# print(story.capitalize())       # Capitalizes first word of the string

print(story.find("was"))       # Finds the first occurrence of the word in the string (only first) and returns their position
# print(story.replace("was", "WOULD BE"))       # Finds & replaces old word with new in the string (all occurrences)


year = '1700'

print(int(year[:2])+1)
print(year[2:])

print(int(float('1.07')))