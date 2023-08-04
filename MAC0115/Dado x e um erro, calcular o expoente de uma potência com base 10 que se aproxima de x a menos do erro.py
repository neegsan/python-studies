x = float(input("x:"))
e = float(input("e:"))

a = 0.0
b = x

while b - a > e :
    y = (b - a) / 2
    if y - log10(x) == 0 :
        print(y)
    elif y - log10(x) > 0 :
        b = y
