l1 = [3,5,8,10,18,20]

# divBy5 = lambda num: True if num % 5 == 0 else False

divBy5 = lambda num: num%5==0   # Same result as the above lambda fn()

print(list(filter(divBy5, l1)))