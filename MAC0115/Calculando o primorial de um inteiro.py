n = int(input("n > 0:"))
x = 2
p = 1
while x <= n :
    y = 2
    while x % y != 0 :
        y = y + 1
    if x == y:
        p = p*x
    x = x + 1
print(p)
