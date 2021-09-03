myDict = {
    'Khata': 'Book',
    'Kalam': 'Pen',
    'Paani': 'Water'
}
print('Your options are: ', myDict.keys())
a = input("Enter a Hindi word (from above list):\t")

# print('The meaning of your word is:\t', myDict[a])  # Will work but the problem with this statement is that it will throw error when the we input a jargon word which is not there in the key list

print('The meaning of your word is:\t', myDict.get(a))  # The get() will return a None if any random word is entered
