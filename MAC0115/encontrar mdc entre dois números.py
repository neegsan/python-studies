m = int(input("Digite m:"))
n = int(input("Digite n:"))
if m < n :
    mdc = n
    while (n % mdc != 0) or (m % mdc != 0) :
            mdc = mdc - 1
    print(mdc)
elif n < m :
    mdc = m
    while (n % mdc != 0) or (m % mdc != 0) :
            mdc = mdc - 1
    print(mdc)
else:
    print(m)
