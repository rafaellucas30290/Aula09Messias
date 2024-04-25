def conta_vogais(string):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in string:
        if letra in vogais:
            contador += 1
    return f'há {contador} vogais nesta frase/palavra'
print(conta_vogais('bom dia'))