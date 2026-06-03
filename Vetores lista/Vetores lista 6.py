"""Verifique se um nome digitado pelo usuário está em uma lista de nomes."""

List_Names=['Gabriel', 'Barriga' , 'Artur' , 'Lara' , 'Dessa' , 'Adri']

Name=input("Qual o seu nome?").title()
if Name in List_Names:
    print(f"O nome {Name.capitalize()} está na lista" )
else:
    print(" Nome não encontrado")