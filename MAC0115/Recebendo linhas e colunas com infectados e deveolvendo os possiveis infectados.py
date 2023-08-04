def teste_reticulado_2d():
    lista = []
    for i in range(len(M)):
        for j in range(len(M[0])):
            if infectados(extrai_linha(M,i)) and infectados(extrai_coluna(M,j)):
                lista.append(M[i][j])
    return(lista)
