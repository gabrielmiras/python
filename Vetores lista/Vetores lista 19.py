"""Simule um carrinho de compras: adicione produtos até que o usuário digite 'fim' e, no final, mostre o carrinho."""

Carrinho=[]

while True:
    compras=input("Digite o produto que quer adicionar ('fim' para sair): ")

    if compras == 'fim' or compras == 'FIM' or compras == 'Fim':
        print("Itens no seu carrinho")
        break
    else:
        Carrinho.append(compras)

