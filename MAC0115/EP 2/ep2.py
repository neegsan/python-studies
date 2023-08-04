# -*- coding: utf-8 -*-

"""
     Nome do aluno: Almir Junior
     Número USP: 11222818
     Curso: Matemática Licenciatura - Noturno
     Disciplina: MAC0110  Introdução à Computação
     Exercício-Programa EP2

          DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
     TODAS AS PARTES ORIGINAIS DESTE EXERCÍCIO-PROGRAMA FORAM
     DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
     DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
     OU PLÁGIO.

         DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESTE
     PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
     ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA SERÃO
     TRATADOS SEGUNDO OS CRITÉRIOS DIVULGADOS NA PÁGINA DA DISCIPLINA.
  
        Para elaborar esse programa utilizei as notas de aula disponíveis
    e também as referências indicadas na página da disciplina no e-disciplinas.
    A referência principal foi, Think Python 2nd Edition by Allen B. Downey.
    O pricipal capítulo consultado foi o que discute sobre funções.
    
"""

print('--------------------------------------------------------------------')
print('\nEste programa imprime o nome do dia da semana e o calendário do mês'
      '\ncorrespondentes a cada uma das n datas fornecidas.')
print('\n--------------------------------------------------------------------')


""" A função dia_semana recebe três inteiros como parâmetro e retorna um
inteiro entre 0 e 7 que representam dias da semana """


def dia_semana(dia, mes, ano):
    b = (14 - mes) // 12
    a = ano - b
    k = a + a//4 - a//100 + a//400
    m = mes + 12*b - 2
    d = dia + k + (31*m)//12
    dia_semana = d % 7

    return (dia_semana)


""" A função dia_nome recebe um inteiro positivo entre 0 e 7 como parâmetro e retorna um
uma string que representa o nome do dia da semana """


def dia_nome(x):
    if x == 1:
        dia_nome = "Segunda-feira"

    elif x == 2:
        dia_nome = "Terça-feira"

    elif x == 3:
        dia_nome = "Quarta-feira"

    elif x == 4:
        dia_nome = "Quinta-feira"

    elif x == 5:
        dia_nome = "Sexta-feira"

    elif x == 6:
        dia_nome = "Sábado"

    else:
        dia_nome = "Domingo"
    return (dia_nome)


""" Início do programa que recebe um inteiro positivo n, solicita n datas na forma
dia, mês e ano e retorna o nome do dia da semana das datas inseridas e o calendário
do mês e ano da data inserida """


i = 0
n = int(input("\nDigite um inteiro positivo para n: "))

while i < n:
    i = i + 1
    print(f"\nData {i}")

    dia = int(input('Digite um inteiro (entre 1 e 31) para o dia: '))
    mes = int(input('Digite um inteiro (entre 1 e 12) para o mês: '))
    ano = int(input('Digite um inteiro (>= 1600) para o ano: '))

    if ano < 1600:
        print(f"\nData fornecida com ano ({ano}) inválido.")
        print('\n-------------------------------------------------')
        last_day = 0

    elif 12 < mes or mes < 1:
        print(f"\nData fornecida com mês ({mes}) inválido.")
        print('\n-------------------------------------------------')
        last_day = 0

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        last_day = 30

        if last_day < dia or dia < 1:
            print(f"\nData fornecida com dia ({dia}) inválido.")
            print('\n-------------------------------------------------')

    elif mes == 2:
        bi = (ano % 400 == 0) or (
            (ano % 4 == 0) and not (ano % 100 == 0))

        if bi == True:
            last_day = 29
        else:
            last_day = 28

        if last_day < dia or dia < 1:
            print(f"\nData fornecida com dia ({dia}) inválido.")
            print('\n-------------------------------------------------')

    else:
        last_day = 31

        if last_day < dia or dia < 1:
            print(f"\nData fornecida com dia ({dia}) inválido.")
            print('\n-------------------------------------------------')

# --------------- Imiprimindo a data e o dia da semana----------------------
    if 1599 < ano and 0 < mes < 13 and 0 < dia < last_day + 1:
        print(
            f"\nData : {dia}/{mes}/{ano} - Dia da semana : {dia_nome(dia_semana(dia, mes, ano))}")
        print(f"\n  Calendário : Mês {mes} - Ano {ano}")
        print("\n  Dom  Seg  Ter  Qua  Qui  Sex  Sab")

# --------------- Imprimindo calendário -----------------------------------

        space = 1
        while space <= dia_semana(1, mes, ano):
            print("     ", end='')
            space = space + 1

        nosl = dia_semana(1, mes, ano)
        num = 1
        while num < last_day + 1:
            nosl = nosl + 1
            if nosl % 7 == 0:
                print(f"{num:5d}")
            else:
                print(f"{num:5d}", end='')
            num = num + 1
        print()
        print('\n-------------------------------------------------')
