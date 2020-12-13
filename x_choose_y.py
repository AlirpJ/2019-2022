import math

x = input("X: ")
y = input("Y: ")
x = int(x)
y = int(y)


#assert x is int
#assert y is int

if x >= y:
    output = math.factorial(x) / ( math.factorial(y)* math.factorial((x-y)) )
    print("- - -")
    print("X Choose Y is:")
    print(output)
else:
    print("Input invalid!")
