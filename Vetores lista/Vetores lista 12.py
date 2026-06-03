"""Substitua todos os números ímpares de uma lista por zero."""
numeros = [10, 5, 23, 1, 0, 8, 15]

for i in range(len(numeros)):
    if numeros[i] % 2 != 0:
        numeros[i] = 0
print("Lista modificada:", numeros)