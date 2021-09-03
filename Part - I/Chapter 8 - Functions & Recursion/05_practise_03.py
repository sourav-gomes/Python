# Find the sum of natural nos

def nSum(num):
    if num > 0:
        return num + nSum(num-1)
    else:
        return num

n = int(input("Enter the count of natural nos.: "))

t =nSum(n)

print(f"Sum of all the first 5 natural nos. is: {t}")