from math import factorial
def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)
a=int(input("enter the number to find the factorial\n"))
print("without recursion")
print("%d%s%d"%(a,",",f(a)))
print("with recursion")
print("%d%s%d"%(a,",",factorial(a)))