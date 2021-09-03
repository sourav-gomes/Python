class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} +"
            index += 1
        return str1[:-1]        # Will not print the end '+' sign. String spicing same as print from 0 one less

    def __add__(self, vec2):
        # vec1Len = Vector.__len__(self.vec)
        # vec2Len = Vector.__len__(vec2.vec)
        vec1Len = len(self.vec)
        vec2Len = len(vec2.vec)
        if vec1Len == vec2Len:
            newList = []
            for i in range(len(self.vec)):
                newList.append(self.vec[i] + vec2.vec[i])
            return Vector(newList)
        else:
            return f"Vec1 Length: {vec1Len} and Vec2 Length: {vec2Len} are NOT Equal. You cannot Add vectors of different lengths"

    def __mul__(self, vec2):
        vec1Len = len(self.vec)
        vec2Len = len(vec2.vec)
        if vec1Len == vec2Len:
            sum = 0
            for i in range(len(self.vec)):
                sum += self.vec[i] * vec2.vec[i]
            return sum
        else:
            return f"Vec1 Length: {vec1Len} and Vec2 Length: {vec2Len} are NOT Equal. You cannot Multiply vectors of different lengths"

    def __len__(self):
        return len(self.vec)

    


v1 = Vector([1,4,6,8])
v2 = Vector([1,6,9,10,15])
# v1 = Vector([1,4,6,56,78,90])   # will print => 1a0 +4a1 +6a2 +56a3 +78a4 +90a5 
print(v1)

''' Generally in python cli if we add 2 lists it just appends check eg below so to add we cannot just use the + 
>>> a = [1,2]
>>> b = [2,3]
>>> a+b
[1, 2, 2, 3]
'''
sum = v1+v2
print(sum)

vectorDotProduct = v1*v2
print(vectorDotProduct)

