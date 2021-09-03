comment = input("Enter the text: ")

if("Harry" in comment):
    spam = True
elif("harry" in comment):
    spam = True
elif("HaRRy" in comment):
    spam = True
elif("HARRY" in comment):
    spam = True
else:
    spam = False

if(spam):    
    print("This post is talking about Harry")
else:
    print("This post is not talking about Harry")