myDict ={
    "Name": "Ham",
    "Class": "5D",
    "Marks": [56, 78, 90],
    "anotherDict": {"Name":"Joseph",
                    "Class": "4C"
                    }
}

print(myDict)       # displays the full Key-value pairs
print(myDict["Name"])   # displays the Name Key-value pairs
print(myDict["Marks"])  # displays the Marks Key-value pairs
print(myDict["anotherDict"]["Name"])    # Dispalys key-value pair within anotherDict

myDict["Marks"]= [67, 99]   # dictionaries are mutable i.e. changeable unlike tuples. However it doesn't append, just overwrites
print(myDict["Marks"])