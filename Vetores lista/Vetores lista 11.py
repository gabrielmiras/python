"""Remova todos os números negativos de uma lista de inteiros."""

print("Removedor de números negativos")

List_Numeros = [1,-2,3,4,5,-6,7,-8,9,10]

List_Numeros = [num for num in List_Numeros if num >= 0]
print(List_Numeros)