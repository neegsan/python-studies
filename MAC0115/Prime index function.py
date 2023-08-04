def prime(n) :
"verifica se um número é primo"
    n = int(input("n > 0:"))
    i = 2
    primo = True
    while i < n and primo :
        if n % i == 0:
            primo = False
    else:
        i = i + 1
    if primo == True :
        return(n)
    
def pi(x) :
"conta quantos primos existem entre 1 e x"
    x = int(input("x>1:"))
    k = 2
    while k <= x :
        print(prime(k))
        k = k + 1
        
    


def index(n):
    k = 2
    r = 2
    s = 0
    while k <= n:
        while r <= k :
            if k % r != 0 :
                r = r + 1
            elif :
        k = k + 1
        r = 2
        return(s)    
