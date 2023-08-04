a = 1
b = 2
c = 3
while a + b + c <= 1000 :
    if a**2 + b**2 == c**2 :
        if a + b + c == 1000 :
            print("é uma tripla", a , b , c)
        else:
            print("não é uma tripla", a , b , c)
            a = a + 1
            b = b + 1
            c = c + 1
    else :
        print("Também não é uma tripla", a , b , c)
        a = a + 1
        b = b + 1
        c = c + 1
        
