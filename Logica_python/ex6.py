distancia = float(input("Distância em Km"))
velo_media = float(input("velocidade média em Km"))
tempo_horas = distancia/velo_media
tempo_minutos = (distancia/velo_media)*60
print(tempo_horas, "h")
print(tempo_minutos, "min")