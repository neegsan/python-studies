n = int(input("n:"))
i = int(input("i:"))
j = int(input("j:"))
m = 0
k = 1
print(0 , end = ' ')
while k < n :
    m = m + 1
    if m % i == 0 :
        print(m , end = ' ')
        k = k + 1
    elif m % j == 0 :
        print(m , end = ' ')
        k = k + 1
    elif m % (i*j) == 0 :
        print(m , end = ' ')
        k = k + 1
