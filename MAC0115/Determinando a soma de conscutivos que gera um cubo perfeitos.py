n = int(input("Digite um número:"))
s = 0
n1 = n*(n - 1) + 1
while s < n**3 :
    if n1 % 2 != 0 :
        s = s + n1
        print(s , n1 ,)
    n1 = n1 + 1
    
