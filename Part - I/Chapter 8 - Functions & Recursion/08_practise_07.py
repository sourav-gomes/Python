'''
a = "      How  are   you?     "
print(a)
print(a.strip())    # strips the string of the opening and closing spaces
print(a.split())    # Split - Returns a list of words in a string

'''

def removeWord(sen, word):
    newStr = sen.replace(word, "")
    return newStr.strip()

sen = "   This is a good boy    "

newSen = removeWord(sen, "good")

print(newSen)


