name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone = int(input("Enter phone number: "))

template = "The name of the student is {1}, his marks are {2} and phone number is {0}.".format(phone, name, marks)
print(template)

# You can also do:

output = template.format(name, marks, phone)
print(output)       # Same output