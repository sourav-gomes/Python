f = open('another.txt')     # open file another.txt in read mode by default
txt = f.read()

'''
# Harry's  way of doing it using string functions 
if 'twinkle' in txt or 'Twinkle' in txt:
    print("Twinkle is present in the file!")
else:
    print("Twinkle is NOT present in the file!")
'''
# Another way of doing it using string functions 
if txt.find("twinkle") > 0 or txt.find("Twinkle") > 0:
    print("Twinkle is present in the file!")
else:
    print("Twinkle is NOT present in the file!")


f.close()