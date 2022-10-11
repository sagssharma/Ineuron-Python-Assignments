import math

a=float(input("Enter a"))
b=float(input("Enter b"))
c=float(input("Enter c"))

s=(a+b+c)/2

area= s*(s-a)*(s-b)*(s-c)
area=area**(0.5)
print("Area of given triangle is ",area)