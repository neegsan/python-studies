n = int(input("n:"))
d = int(input("d:"))
c = 0
while n > 0 :
    if n % 10 == d :
        c = c + 1
        n = n // 10
    if n % 10 != d:
        n = n // 10
print(c)
    
