def tam(numero):
    cifra = 0

    while numero/10 >= 1:
        cifra = cifra + 1
        numero = numero/10

    cifra = cifra + 1
    return cifra

def partes(numero, posicion):
    longNum = len(numero)
    partes = longNum/3
    indice = 0
    s2 = 