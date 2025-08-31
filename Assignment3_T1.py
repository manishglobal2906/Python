print("***Program of Factorial***")
def factorial(n):
    if (n==0) | (n==1):
        return 1
    else:
        return n*factorial(n-1)

x=int(input("Enter a number: "))
if x<0:
    print("Please enter a number greater than or equ(al to zero")
else:
    num=factorial(x)
    print("The factorial of",x,"is: ",num)
