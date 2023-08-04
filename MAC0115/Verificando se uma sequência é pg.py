n = float(input("Tamanho da sequência:"))
anterior = float(input("Primeiro termo:"))
atual = float(input("Próximo termo:"))
razao = atual / anterior
pg1 = True
n = n - 2
while 0 < n :
    n = n - 1
    anterior = atual
    atual = int(input("Próximo termo:"))
    pg =(atual / anterior == razao ) and pg1
print(pg)
    
