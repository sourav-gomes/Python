class Sample:
    a = 'Class Attribute'

obj = Sample()

obj.a = 'Instance/Object Attribute'

print(Sample.a)         # print class attribute 'a'
print(obj.a)            # print instance/object attribute 'a'

# So conclusion changing of Instance attribute 'a' does not change class attribute 'a'

# If you want to change Class attribute use the following command
Sample.a = 'Class Attribute Changed'
print(Sample.a)
