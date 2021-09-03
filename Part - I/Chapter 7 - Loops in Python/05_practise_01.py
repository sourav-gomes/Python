n = int(input("Enter a number\n"))

for i in range(1, 13):
    # print(str(n) + " x " + str(i) + " = " + str(n*i))     # using concatenation
    # print(str(n), "x", str(i), "=" + str(n*i))              # using , & concatenation
    print(f"{n}x{i}={n*i}")                                 # using fstrings

