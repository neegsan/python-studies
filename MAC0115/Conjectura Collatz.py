a = int(input("Dê um número:"))
while a != 1:
    print(a, end =' ')
    if a % 2 == 0:
        a = a // 2
    else:
        a = 3*a + 1
print(a)
