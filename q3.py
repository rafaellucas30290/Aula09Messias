def converte_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return f'{horas:02}:{minutos:02}:{segundos_restantes:02}'
print(converte_tempo(300))