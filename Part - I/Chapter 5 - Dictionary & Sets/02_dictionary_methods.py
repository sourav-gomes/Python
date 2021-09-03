myDict ={
    "name": "Ham",
    "class": "5D",
    "marks": [56, 78, 90],
    "anotherdict": {'name':'Joseph',
                    'class': '4C'
                    },
    1: 33
}

# Dictionary Methods

# print(myDict.keys())        # Print the keys of the dictionary
# print(list(myDict.keys()))        # Print the keys of the dictionary in list typecast 
# print(myDict.values())        # Print the values of the dictionary
# print(myDict.items())        # Print all the (key, values) of the dictionary for all contents, in tuples format

# print(myDict)

updateDict = {
    'Shahrukh': 'Khan',
    1: 111
    }

myDict.update(updateDict)   # Updates the dictonary by adding key-value pairs

# print(myDict)

print(myDict['Shahrukh'])       # Prints value associated with Key 'Shahrukh'
print(myDict.get('Shahrukh'))       # Prints value associated with Key 'Shahrukh'

# Difference b/w above 2 statements

print(myDict.get('Aamir'))       # Returns 'None' if associated key not present in dictionary. In this case 'Aamir'
print(myDict['Aamir'])      # Returns Error if associated key not present in dictionary. In this case 'Aamir'




