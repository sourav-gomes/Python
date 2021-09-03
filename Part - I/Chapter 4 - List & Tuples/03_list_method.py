l1 = [5,9,3,6,2,43,6]
print(l1)
l1.sort()       # sorts the list ascending order
# l1.reverse()    # reverses the list
# l1.append(85)   # append 85 at the end of the list
# l1.insert(3,444)    # Inserts 444 at index 3
# l1.pop(4)           # removes element at index 4
l1.remove(6)    # removes 6 from the list, ONLY first instance
print(l1)
elements = [2,1,4,3]
elements1 = [1,2,3,4]
elements2 = [4,3,2,1]
# print(arrayArrange(elements))

# elements.sort()
# print(elements)
# elements.reverse()
# print(elements)
# elements.sort(reverse = True)
# print(elements)

# c = l1[0] + l1[1]
# print(c)

# Printing array in reverse order
for i in range(len(elements)-1,-1,-1):
    print(elements[i], end = " ")

# if elements == elements1:
#     print("True")
# print("False")
print(elements)
if elements1 == elements.sort():
    print("True")
print("\nFalse")
print(elements1)
print(elements)

