## Covert   inches --> cms

def convert(inch):
    return inch*2.54

inch = int(input("Enter length (in inches) : "))

cen = convert(inch)

print(f"The length (in centimeters) is: {cen}cm")