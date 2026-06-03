"""Faça um programa que leia 10 números e armazene em duas listas: uma com pares e outra com ímpares."""

Pares=[]
Impares=[]

for x in range(10):
    Numero=float(input("Digite 10 números:"))
    if Numero%2==0:
        Pares.append(Numero)
    else:
        Impares.append(Numero)
print(f"Os Números pares foram {Pares} \n")
print(f"Os Números Impares foram {Impares}")