n = int(input("Vamos calcular a soma de todos números pares menores do que n. Dê um valor para n:"))
p = 2
s = 0
while p < n :
    if p % 2 == 0 :
        s = p + s
        p = p + 1
    else:
        p = p + 1

print("A quantidades de números pares menores do que", n " é:" , c)
