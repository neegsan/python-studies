n = int(input("Um número inteiro é triangular se é produto de três números consecutivos. Vamos verificar se um número n é triangular. Dígite um valor para n:"))
m = 2
while n > 1 :
    if ( n % m == 0 ) and ( n % (m + 1) == 0 ) and ( n % (m + 2) == 0 ):
        print("sim")
        m = m - 1

    else :
        m = m - 1
