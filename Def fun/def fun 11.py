""" 11. Desafio Final (Avançado)
Simule um sistema de cadastro de produtos com as seguintes opções:

1 - Cadastrar produto
2 - Listar produtos
3 - Buscar produto pelo nome
4 - Sair
Use uma lista para armazenar os produtos.
Crie funções para cada opção.
Utilize laços de repetição e estruturas de decisão junto com funções."""

lista_produtos=[
    {"id": 1, "nome": "Notebook"},
    {"id": 2, "nome": "Mouse"},
    {"id": 3, "nome": "Teclado"}
]

def listar():
    if not lista_produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de produtos cadastrados.")
        for produto in lista_produtos:
            print(f"ID: {produto['id']} | Nome: {produto['nome']}")


def buscar_produto():
    search = input("Digite o nome do produto que deseja buscar: ")
    achou = False
    for produto in lista_produtos:
        if produto["nome"].lower() == search.lower():
            print(f" Produto encontrado! ID: {produto['id']} | Nome: {produto['nome']}")
            achou = True
            break
    if not achou:
        print(" Esse produto não está cadastrado.")


def saindo():
    print("Obrigado por utilizar o software 👍")

def cadastrar_produto():
    id_produto = int(input("Digite o id do produto: "))
    for produto in lista_produtos:
        if produto["id"] == id_produto:
            print("️ Erro: Já existe um produto com este ID!")
            return
    nome_produto = input("Digite o nome do produto: ")
    lista_produtos.append({"id": id_produto, "nome": nome_produto})
    print("O produto foi cadastrado na lista de produtos \n")


while True:
    user = int(input("O que deseja realizar ? Cadastro (1), Listar produtos (2), Buscar produto (3),Sair (4): \n"))
    if user==4:
        saindo()
        break

    elif user==1:
        cadastrar_produto()

    elif user==2:
        listar()

    elif user==3:
        buscar_produto()
    else:
        print("Opção inválida, digite: Cadastro (1), Listar produtos (2), Buscar produto (3),Sair (4): \n  ")
