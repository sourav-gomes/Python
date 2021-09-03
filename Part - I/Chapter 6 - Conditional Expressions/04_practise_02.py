sub1 = int(input("Enter markes of subject 1: "))
sub2 = int(input("Enter markes of subject 2: "))
sub3 = int(input("Enter markes of subject 3: "))

if(sub1 < 33 or sub2 < 33 or sub3 < 33 ):
    print("You have failed since you have marks of at least 1 subject < 33")
elif((sub1+sub2+sub3)/3 < 40 ):
        print("You have failed since your aggregate is < 40")
else:
    print("Congratulations! You have passed.")