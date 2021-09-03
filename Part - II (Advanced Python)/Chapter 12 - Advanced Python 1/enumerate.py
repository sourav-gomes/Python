# enumerate(list_name): Enumerate function adds counter to an iterable and returns it

list1 = [45, 87.9, True, 'Joseph']
i=0
for item in list1:
    print(i, item)      # will print the index & item of the list
    i += 1

# The above function using the enumerate():

for index, items in enumerate(list1):
    print(items, index)     # you can also print(index, items)