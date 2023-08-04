print("Vamos verificar em uma sequência de n numeros qual é o comprimento da maior subsequência dessa sequência!")
n = int(input("n:"))
anterior = int(input("numero:"))
maior = 1
comprimento = 1
while n > 1:
    n = n - 1
    atual = int(input("numero:"))
    if anterior < atual :
        comprimento = comprimento + 1
        maior = comprimento
    if atual <= anterior :
        comprimento = 1
    anterior = atual
print(maior)   
