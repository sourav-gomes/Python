n = 3

for i in range(3):
    print(" " * (n-i-1), end = "")      # end="" omits the default line gap
    print("*" * (2*i+1), end = "")
    print(" " * (n-i-1))
