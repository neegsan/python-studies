n = int(input("n:"))
h3 = 0
i = n
c = 0
while h3 <= n:
    while i > 0:
        y = 1/i - c
        t = h3 + y
        c = (t - h3) - y
        h3 = t
        i = i - 1
    print(h3)
