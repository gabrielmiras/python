"""Leia 10 números e ordene a lista do maior para o menor."""

Lista=[]
for x in range(10):
    numeros_lista=int(input("Digite 10 números :"))
    Lista.append(numeros_lista)
    Lista.sort()
print(Lista)