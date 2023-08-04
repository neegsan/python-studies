n = int(input("Tamanho da sequência:"))
anterior = int(input("Primeiro termo:"))
atual = int(input("Próximo termo:"))
razao = atual / anterior
pg = True
n = n - 2
while 0 < n :
    n = n - 1
    anterior = atual
    atual = int(input("Próximo termo:"))
    if atual / anterior != razao :
        pg = False
print(pg)
    
