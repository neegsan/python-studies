n = int(input("Dê um número:"))
primo = True
i=2
while i < n and primo: #vai levar em conta se o anterior era primo ou nao
    primo = (n % i != 0)
    i = i+1
print(primo)
