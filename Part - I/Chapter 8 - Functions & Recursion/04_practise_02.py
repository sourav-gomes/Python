'''
def convert(cel):
    return (cel*9/5) + 32

cel = int(input("Enter the temperature in Celcius: "))

fht = convert(cel)

print(f"The temperature in Farenheit is: {fht}")

'''

#########################

# Q3

print("How", end="")       # end="" means same line with no space 
print("are", end="")       # Output: Howareyou?
print("you?")

print("How", end=" ")       # end=" " means same line with 1 space means adds onespace after every print
print("are", end=" ")       # Output: How are you?
print("you?")

print("How", end="\t")       # end="\t" means same line with tab space means adds one tab space after every print
print("are", end="\t")       # Output: How     are     you?
print("you?")

print("How", end="\n")       # end="\n" - The default behaviour, means diff/next line every print
print("are", end="\n")       # Output: default out put in3 diff lines
print("you?")