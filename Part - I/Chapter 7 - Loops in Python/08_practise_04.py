num = int(input("Enter a number: "))

isPrime = True

for i in range(2, num):
    if num % i == 0:
        isPrime = False
        break
    
if isPrime:
    print(f"{num} is a Prime number")
else:
    print(f"{num} is a not a Prime number")


