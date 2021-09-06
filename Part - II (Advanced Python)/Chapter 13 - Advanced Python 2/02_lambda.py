# Lambda functions: Functions created using an expression using 'lambda' keyword
# It can be used as a normal function. Usually done when trying to pass function as argument

## NORMAL FUNCTION AS WE WRITE

def func(a):
    return a+5

x = 40
print(func(x))      # This will print 45

## WRITING THE SAME fUNCTION USING LAMBDA

func = lambda a: a+5

print(func(x))      # This will print same 45

## SIMILARLY WRITING LAMBDA FUNCTION FOR SUM & SQUARE 

square = lambda b: b*b

sum = lambda a,b,c : a+b+c


print(square(x))      # This will print 40x40 = 1600

print(sum(x,10, 30))    # This will print 40+10+30 = 80

