# NAO MODIFICAR A LINHA ABAIXO
from testagem import infectados_em, num_individuos, num_testes, envia

# MODIFICAR A PARTIR DAQUI
N = num_individuos()
resposta = 0 # inteiro representando estado dos individuo tal que: 
             #   digito i = 0: individuo i nao esta infectado
             #   digito i = 1: individuo i esta infetcado

# Testagem por particionamento binario
i = 0
while i < N:
	n = N-i # numero de individuos sendo testados testados
	while n >= 1:
		if infectados_em(i,n+i) == True:
			if n % 2 == 0:
				n = n // 2
			elif n == 1 :
				resposta = respota + 2**i
				i = i + 1
				n = N - i
			elif n % 2 != 0:
				n = (n + 1) // 2
		else:	
			if n == 1:
				reposta = resposta + 2**(N-(i+2))
				i = n + i + 1
				
			else :
				i = n + i
				n = 0

# Submeter resultado dos testes
envia(resposta)
