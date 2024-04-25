def encontra_palavras(lista_palavras, letra):
    palavras_iniciadas_com_letra = [palavra for palavra in lista_palavras if palavra.startswith(letra)]
    return palavras_iniciadas_com_letra


print(encontra_palavras(['Abóbora', 'Avião', 'Burro', 'Braço', 'Carro', 'Cavalo', 'Dado', 'Doido', 'Elo', 'Entender'], 'A'))

