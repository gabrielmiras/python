"""Leia uma lista de números e crie uma nova lista apenas com os valores únicos (sem repetições)."""

lista = [80, 20, 30, 20, 50, 60, 70, 80]
lista_unicos = []

for num in lista:
    if num not in lista_unicos:
        lista_unicos.append(num)
        lista_unicos.sort()
print("Lista sem repetições :", lista_unicos)