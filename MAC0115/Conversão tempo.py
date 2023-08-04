tempo = int(input("Tempo:"))
dias = tempo //1440
horas = (tempo % 1440)//60
minutos = ((tempo % 1440)%60)
print(dias, horas, minutos)
