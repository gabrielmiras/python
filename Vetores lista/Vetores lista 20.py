"""Desenvolva um menu de opções para gerenciar uma lista de tarefas: adicionar, remover, exibir e sair."""

Lista_de_tarefas=[]

def mostrar_lista():
    print(f"{Lista_de_tarefas}")
    if len(Lista_de_tarefas) == 0:
        print("Sua lista de tarefas está vazia! 📭")
    return Lista_de_tarefas

while True:
    opcao = float(input("O que deseja realizar ? (Adicionar tarefa (1) , Remover Tarefa (2) , Exibir Tarefas já existentes (3) , Sair (4): "))
    if opcao == 4:
        print("Programa finalizado com sucesso")
        break
    if opcao == 1:
        add_tarefa=input("Adicione um tarefa:")
        Lista_de_tarefas.append(add_tarefa)
    if opcao == 2:
        remover_tarefa = input("Digite o nome da tarefa que deseja remover: ")
        if remover_tarefa in Lista_de_tarefas:
            Lista_de_tarefas.remove(remover_tarefa)
            print(f"Tarefa '{remover_tarefa}' removida com sucesso!")
        else:
            print("Essa tarefa não foi encontrada na lista.")

    if opcao == 3:
        print("Essas são as tarefas existentes na lista: \n")
        mostrar_lista()