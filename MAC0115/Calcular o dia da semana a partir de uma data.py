d = int(input("dia:"))
m = int(input("mes:"))
a = int(input("ano:"))

if m == 1 :
    m = 13
    a = a - 1
if m == 2 :
    m = 14
    a = a - 1
s = ( d + (13*(m+1))//5 + a + a//4 - a//100 + a//400 ) % 7
print("O dia da semana é:"s)
