# Problem #9 - Delete the contents of a file

filename = "this_copy.txt"
content = ""

with open(filename,'w') as f:
    f.write(content)            # alternatively you could have wtitten: f.write("") without declaring content variable