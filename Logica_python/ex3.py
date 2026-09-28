Dias = int(input("quantos dias?"))
Horas = int(input("quantas horas?"))
minutos = int(input("quantos minutos"))
dias_em_segundos = Dias*86400
horas_em_segundo = Horas*3600
minutos_em_segundos = minutos*60
soma = dias_em_segundos + horas_em_segundo + minutos_em_segundos
print("valores convertidos todos em segundos: " , soma )