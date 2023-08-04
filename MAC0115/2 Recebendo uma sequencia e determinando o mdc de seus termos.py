n = int(input("Tamanho da sequencia:"))
a1 = int(input("Primeiro termo:"))
m = 1
while m < n :
    m = m + 1
    a2 = int(input("Proximo termo:"))
    if a1 < a2 :
        mdc = a2
        while (a1 % mdc != 0) or (a2 % mdc != 0) :
            mdc = mdc - 1
    elif a2 < a1 :
        mdc = a1
        while (a1 % mdc != 0) or (a2 % mdc != 0) :
            mdc = mdc - 1
    a1 = mdc
print(mdc)
