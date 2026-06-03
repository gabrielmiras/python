"""Faça um programa que leia números do usuário até que ele digite 0. Depois, mostre a lista e a soma dos números."""

List_Numeros = []
while True:
    numeros = float(input("Digite o número que será armazenado ( Digite 0 para sair): "))
    List_Numeros.append(numeros)
    if numeros == 0:
        print(f"{List_Numeros}")
        break