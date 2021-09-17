# l1 = [i*7 for i in range(1,11)]     # This will generate a list of 7 times table
# print(l1)   # Output - [7, 14, 21, 28, 35, 42, 49, 56, 63, 70], BUT all values are Integer

# To print 7 times table in separate lines we will use .join()
# But remeber the list l1 contains integer values. So to convert it into string we will use the following

l1 = [str(i*7) for i in range (1,11)]

print(l1)   # will print ['7', '14', '21', '28', '35', '42', '49', '56', '63', '70']

timeTable = "\n".join(l1)

print(timeTable)