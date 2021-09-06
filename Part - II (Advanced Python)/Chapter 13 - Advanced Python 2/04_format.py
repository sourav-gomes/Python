# Format method does the same as f"" (f string) used in Python3 before that format method was used

name = "Joseph"
age = 14
gender = "male"

## USING f"" string to print
print(f"Hello! I'm {name}. I'm a {gender} of {age} years")

## USING format method to print the same

a = "Hello! I'm {}. I'm a {} of {} years".format(name, gender, age)
print(a)

a = "Hello! I'm {}. I'm {} years old. And I'm a {}".format(name, gender, age)     # order not changed, so prints wrong
print(a)

a = "Hello! I'm {0}. I'm a {2} of {1} years".format(name, age, gender)     # order changed so the index nos of variables to be printed also changes
print(a)