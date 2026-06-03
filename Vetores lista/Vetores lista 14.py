"""Crie uma lista com 5 strings e conte quantas começam com a letra 'A'."""

palavras = ["Abajur", "bola", "Amigo", "caneta", "avião"]
contador_A = 0
for texto in palavras:
    if texto.upper().startswith('A'):
        contador_A += 1

print(f"Quantidade de strings que começam com 'A': {contador_A}")