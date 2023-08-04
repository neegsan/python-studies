n = int(input("Digite n: "))     #tamanho da sequência 
anterior = int(input("Número:")) #primeiro termo
maior = 0 
comprimento = 1
while n > 1:
    n = n - 1
    atual = int( input("Número:"))
    if atual > anterior :
         comprimento = comprimento + 1
         maior = comprimento
         print(comprimento, maior)
    else :
        comprimento = 0
        print(comprimento, maior)
        comprimento = 1
                 
if comprimento > maior :
    maior = comprimento
anterior = atual
print(maior)

