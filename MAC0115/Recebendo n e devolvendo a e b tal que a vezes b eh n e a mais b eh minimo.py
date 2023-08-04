n = int(input("Digite n:"))
i = 1
a = 0
b = 0
s = n+1
while i < n + 1:
    if n % i == 0 :
        if i + n // i <= s:
            a = i
            b = n // i
            s = a + b
        i = i + 1
    else :
        i = i + 1
if a <= b:
    print(a,b)
else:
    print(b,a)
