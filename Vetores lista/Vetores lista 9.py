"""Crie uma lista com 5 notas de alunos, calcule a média e diga quais alunos ficaram acima da média."""

Alunos=['Zeu','Pelin','Zizou','Armando','Boludo']
Notes=[10,7,6,9,7]

media = sum(Notes)/len(Notes)

print(f"A média da turma foi {media}")
print("Alunos que ficaram acima da média:")

for i in range(len(Notes)):
    if Notes[i] > media:
        print(f"- {Alunos[i]}: Nota {Notes[i]}")
