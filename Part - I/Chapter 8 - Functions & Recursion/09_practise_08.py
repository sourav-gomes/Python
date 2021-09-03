def tables(num):
    for i in range(12):
        print(f"{num}x{i+1}= {num*(i+1)}")

n = int(input("Enter a number: "))

tables(n)

