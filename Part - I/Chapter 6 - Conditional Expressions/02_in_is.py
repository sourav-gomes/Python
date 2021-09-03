a = None           

print(type(a))      # datatype is NoneType

# IS operator

if(a is None):
    print("Yes")
else:
    print("No")

# Same thing can be done with ==

if(a == None):
    print("Yes")
else:
    print("No")


# IS operator

a = [56, 22,23]

print(45 in a)      # Returns False since 45 is not present in list a
print(22 in a)      # Returns True since 45 is present in list a
