## Problem #9: Find out if a file is identical and matches the contents of another file

with open('this.txt') as f:
    file1 = f.read()

with open('this_copy.txt') as f:
    file2 = f.read()

if file1 == file2:
    print(f"Both the files are identical")
else:
    print(f"Both the files are not identical")

