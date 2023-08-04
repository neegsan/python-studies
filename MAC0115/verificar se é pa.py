n = int(input("tamanho da sequencia(n>2):"))

anterior = int(input("primeiro termo:"))
atual = int(input("segunto termo:"))
r = atual - anterior
n = n - 2
eh_pa = True

while n > 0 :
    eh_pa = ( atual - anterior == r ) and eh_pa
    n = n - 1
    anterior = atual
    atual = int(input("numero:"))
    
print(eh_pa)
