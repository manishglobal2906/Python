import math
num=int(input("Enter a number: "))
if num<0:
    print("Please enter a number greater than or equal to zero")
else:
    print("Square root : ",math.sqrt(num))
    print("Logarithm :",math.log(num))

print("Sine is",math.sin(num))
