def readFile(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"{filename} is not found")


readFile("1.txt")
readFile("2.txt")      # this file is missing and need to handle this exception
readFile("3.txt")      # this file is missing and need to handle this exception
