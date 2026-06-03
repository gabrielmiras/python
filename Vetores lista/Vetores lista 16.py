"""Junte duas listas e remova os elementos repetidos."""

lista = ['Caixa','Prateleira','Fruta']
lista2=['Brinde','Fruta','Caixote']

listas_justas= lista+lista2

lista_final = list(set(listas_justas))
lista_final.sort()
print(lista_final)

