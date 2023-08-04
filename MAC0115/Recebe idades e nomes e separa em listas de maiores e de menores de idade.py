idade_pessoas = [7,38,19,28,3,1,2]
maiores_de_idade = []
menores_de_idade = []

while len(idade_pessoas) >= 0:
    pessoas = list(idade_pessoas.keys())
    pessoa = pessoas[0]

    if idade_pessoas[pessoa] >= 18:
        maiores_de_idade.append(pessoa)
    else :
        menores_de_idade.append(pessoa)
    del idade_pessoas[pessoas]
