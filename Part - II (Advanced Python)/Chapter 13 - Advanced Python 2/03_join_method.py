# Join method (strings): Creates a string from iterable objects (i.e. Lists, tuple etc). 

list = ["Camera", "Laptop", "iPad", "Mobile"]

makeString1 = "and".join(list)
makeString2 = "++".join(list)
makeString3 = "\n".join(list)

print(makeString1)       # This will print a STRING "CameraandLaptopandiPadandMobile"

print(makeString2)       # This will print a STRING "Camera++Laptop++iPad++Mobile"

print(makeString3)       # This will print a Camera, Laptop, iPad, Mobile --> In different lines, BUT ONE string

print(type(list))
print(type(makeString1))    # Type would specify as string... <class 'str'>

## NOW SAME THING WITH TUPLE

tuple = ("Camera", "Laptop", "iPad", "Mobile")

makeString1 = "and".join(list)
makeString2 = "++".join(list)
makeString3 = "\n".join(list)

print(makeString1)       # This will print a STRING "CameraandLaptopandiPadandMobile"

print(makeString2)       # This will print a STRING "Camera++Laptop++iPad++Mobile"

print(makeString3)       # This will print a Camera, Laptop, iPad, Mobile --> In different lines, BUT ONE string

print(type(tuple))
print(type(makeString1))    # Type would specify as string... <class 'str'>
