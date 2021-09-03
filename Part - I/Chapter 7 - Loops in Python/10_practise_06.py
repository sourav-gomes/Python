# n! = 1x2x3...xn
# 5! = 1x2x3x4x5

factorial = 1

num = int(input("Enter the number for factorial: "))

for i in range(1, num+1):
    factorial = factorial * i

print(f"The factorial of {num} is {factorial}")
