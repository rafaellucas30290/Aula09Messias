def verificar_primo(numero):
    if numero <1:
        return False
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True
print(verificar_primo(7))
