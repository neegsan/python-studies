n = int(input("Digite n:"))
m = 0
while n > 0 :
    m = 10*m + (n % 10)
    n = n // 10
while m > 0 :
    k = m % 10 
    if ( m // 10 ) % 10 ==  k : 
        m = m // 10
    else :
        m = m // 10
        print(k, end = '')    
