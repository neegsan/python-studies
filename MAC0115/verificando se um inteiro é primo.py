n = int(input("Dígite n > 0:"))
i = 2
primo = True
while i < n and primo :
    if n % i == 0:
        primo = False
    else :
        i = i + 1
print(primo)
