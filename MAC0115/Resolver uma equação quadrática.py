from math import sqrt
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

x_2 = (-b+sqrt(b**2 - 4*a*c))/(2*a)
x_1 = (-b-sqrt(b**2 - 4*a*c))/(2*a)

print(x_1,x_2)
