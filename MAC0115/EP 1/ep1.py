def dia_semana(x,y,z):

    n = int(input("Digite um inteiro positivo para n:"))
    i = 0

    while i < n:
        print()
        print("Par", i+1)
        print()
        nome = input("Digite um nome:")
        print()
        print("A seguir você deve fornecer uma data (dia, mês e ano).")
        print()
        dia = int(input("Digite um número inteiro entre 1 e 31 para o dia?"))
        print()
        mes = int(input("Digite um inteiro entre 1 e 12 para o mês:"))
        print()
        ano = int(input("Digite um inteiro maior que 1599 para o ano:"))
        i = i + 1
        b = (14 - mes) // 12
        a = ano - b
        k = a + a//4 - a//100 + a//400
        m = mes + 12*b - 2
        d = dia + k + (31*m)//12

        dia_semana = d % 7

        if dia_semana == 1:
            dia_semana = "Segunda-feira"

        elif dia_semana == 2:
            dia_semana = "Terça-feira"

        elif dia_semana == 3:
            dia_semana = "Quarta-feira"

        elif dia_semana == 4:
            dia_semana = "Quinta-feira"

        elif dia_semana == 5:
            dia_semana = "Sexta-feira"

        elif dia_semana == 6:
            dia_semana = "Sábado"

        else:
            dia_semana = "Domingo"

        print()
        print(nome, "nasceu", dia_semana)


"""
dia_semana() """
