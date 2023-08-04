n = float(input("Tamanho dea sequência:"))
a1 = float(input("Primeiro termo:"))
a2 = float(input("Segundo termo:"))
a3 = float(input("Terceiro termo:"))
a4 = float(input("Quarto termo:"))
SL = True
n = n - 4
if (a2 != 0) and (a2**2-a1*a3 != 0) :
    p = (a2*a3-a1*a4)/(a2**2-a1*a3)
    q = (a3*p - a4)/ a2
    while 0 < n :
        n = n - 1
        a1 = a2
        a2 = a3
        a3 = a4
        a4 = float(input("Próximo termo:"))
        Lucas = (a4 == p*a3 - q*a2) and SL
    print(Lucas)
else :
    print(not(SL))
