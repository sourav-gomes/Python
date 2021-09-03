letter = '''\nDear <NAME>,\n
Greetings of the day!

We are pleased to inform you that you have been selected.

Have a great day ahead!

Regards,
Joseph

<DATE>
'''
name = input("Enter Your Name: ")
date = input("Enter Date: ")

letter = letter.replace("<NAME>", name)
letter = letter.replace("<DATE>", date)

print(letter)
