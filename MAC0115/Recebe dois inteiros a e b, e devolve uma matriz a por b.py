a = int(input("Digite a:"))
b = int(input("Digite b:"))
matriz = []
for i in range(a) :
    linha = []
    for j in range(b) :
        x = i*b+j
        linha.append(x)
    matriz.append(linha)
print(matriz)
