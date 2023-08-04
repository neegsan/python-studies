from math import sqrt

a = int(input('Diga um valor não nulo para o coeficiente a:'))
b = int(input('Dê um valor qualquer para o coeficiente b:'))
c = int(input('Determine um valor para a constante c:'))
d = b**2 - 4*a*c
if d > 0 :
    x_1 = (-b+sqrt(d))/(2*a)
    x_2 = (-b-sqrt(d))/(2*a)
    if x_1 < x_2 :
        print(x_1,x_2)
    else :
        print(x_2,x_1)
elif d == 0 :
    print(-b/2*a)
else:
    print("0")
