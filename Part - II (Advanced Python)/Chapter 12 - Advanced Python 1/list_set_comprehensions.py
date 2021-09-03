## List comprehensions is an elegant way to create a new list based on existing lists

## OLD|LONG Way

a = [2, 5, 56, 77, 89, 10]
b = []

for items in a:
    if items % 2 == 0:      # will find out all even nos.
        b.append(items)     # add those even nos. to a new list b

print(b)        # print the new list b with only the even nos. from list a. Output --> [2, 56, 10]


# Same thing usig LIST COMPREHENSIONS

b = [i for i in a if i%2==0]    # Just a SHORT-CUT way of writing a 3-line code in 1-line

c = [items for items in a if items>20]    # another way using 'items' instead of 'i' and condition is any no. > 20

print(b)        # Same output --> [2, 56, 10]

print(c)        # Displays list c with all nos > 20, output --> [56, 77, 89]

## SET COMPREHENSIONS: SAME LIKE LIST COMPREHENSION EXCEPT IT CREATES A SET FROM A GIVEN LIST
## ***IMP: SET DOES NOT CONTAIN REPETITIVE|DUPLICATE VALUES

l = [2, 1, 3, 2, 4, 6, 1, 3, 1]

s = {i for i in l}

print(s)            # Output --> {1, 2, 3, 4, 6}, will contain only one instance of a value


