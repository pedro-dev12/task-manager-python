def mostrar_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

tarefas = []

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nLista de tarefas:")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. {tarefa}")

    elif opcao == "3":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
