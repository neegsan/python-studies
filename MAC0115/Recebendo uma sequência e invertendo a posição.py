lista = []
copia = []
n = int(input("Digite o tamanho da sequencia:"))
i = 0
while i <= n - 1:
    x = int(input("Digite um elemento da sequencia:"))
    lista.append(x)
    copia.append(x)
    i = i + 1
    #print(copia, lista)
i = 0
while i <= n - 1:
    lista[i] = copia[n-1-i]
    lista[n-1-i] = copia[i]
    i = i + 1
print(lista)
