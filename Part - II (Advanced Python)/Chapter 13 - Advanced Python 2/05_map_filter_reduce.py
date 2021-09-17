#****************************
# 1. MAP applies a Fn() to all the items in an input list. The fn() can also be a Lamda fn()
#****************************
# NORMAL WAY: Writing a square function from a list and printing the same squared values to a list
# ++++++++++++++++++++++++++++++
def square(num):
    return num*num

l1 = [3, 4, 5]
l2 = []

for i in l1:
    l2.append(square(i))

print(l2)       # Output - [9, 16, 25]

# ++++++++++++++++++++++++++++++

# Method 2: Using Map 

# print(map(square, l1))      # This will print the map object - <map object at 0x7f2e0fb77730>

print(list(map(square, l1)))    # Typecasting the map object to list. Same Output - [9, 16, 25] wrting only 1 sentence

sqr = lambda num : num*num

print(list(map(sqr, l1)))    # Same using 'lambda' fn()

#****************************
# 2. FILTER creates a list of items for which the fn() returns True. The fn() can also be a Lamda fn()
#****************************

def find_num_greater_than_5(num):

    if num > 10 :
        return True
    else :
        return False

l1 = [1,2,4,6,7,8,34,45,68,78,90]

# print(filter(find_num_greater_than_5, l1))  # Filters & create a list with all the values > 10. Prints the filter object <filter object at 0x7f8e0b4cf730>.

print(list(filter(find_num_greater_than_5, l1)))    # Typecasting the <filter object at 0x7f8e0b4cf730> to list.

num_gt_20 = lambda num : True if num > 20 else False

print(list(filter(num_gt_20, l1)))      # Same using 'lambda' fn()


#****************************
# 3. REDUCE applied rolling computation to sequential pair of   elements. The fn() can also be a Lamda fn()
#****************************

from functools import reduce    ## IMP: You need to IMPORT REDUCE

l3 = [1,2,3,4]

rollSum = lambda a,b : a+b   # This fn() will add 2 elements in the list

val = reduce(rollSum, l3)   # This fn() will do a rolling sum i.e. in list l3 it will add [(1+2)= 3, then (3+3)=6, then (6+4)=10. Will return 10]

print(val)

# Similarly writing the same function for rolling multiplication

rollMul = lambda a,b : a*b 

print(reduce(rollMul,l3))   # Will give the product 1x2x3x4 = 24

