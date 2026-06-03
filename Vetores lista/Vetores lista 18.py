"""Faça uma função que recebe uma lista e retorna outra com os elementos em ordem reversa (sem usar .reverse() ou [::-1])."""


def inverter_lista(lista_original):
    lista_invertida = []
    for i in range(len(lista_original) - 1, -1, -1):
        lista_invertida.append(lista_original[i])

    return lista_invertida

minha_lista = [int(input("Digite N1:")), int(input("Digite N2:")), int(input("Digite N3:")), int(input("Digite N4:")), int(input("Digite N5:"))]
resultado = inverter_lista(minha_lista)

print(f"Lista original: {minha_lista}")
print(f"Lista invertida: {resultado}")