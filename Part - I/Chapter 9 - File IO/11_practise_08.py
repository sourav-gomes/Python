# Problem #8 - Making a copy of the this.txt

with open('this.txt') as f:
    text = f.read()

with open('this_copy.txt','w') as f:
    f.write(text)

