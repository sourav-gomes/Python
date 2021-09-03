for i in range(8):          # By default range starts from 0 an ends at n-1 i.e 7 (8-1)
    print(i)

for i in range(1,8):          # If you want range to start from 1. Will print 1-7
    # print("hi")
    print(i)

for i in range(2,8,2):          # Range starts from 2 an ends at n-1 i.e 7 (8-1) with step-size 2 i.e. prints every alternate nos (gap of 2) i.e. 2, 4, 6
    print(i)

# for... range... else

for i in range(10):      
    print(i)
else:
    print("This is an example of for... else")

for i in range(10):
    print(i)
    if i == 5:
        break

else:
    print("This is an example of for... else")      # This time else will not execute since it only executes on successful completion of the loop. Since there's a break so else will not print


