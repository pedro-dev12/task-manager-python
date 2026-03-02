def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as arquivo:
            return [linha.strip() for linha in arquivo.readlines()]
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open("tarefas.txt", "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(tarefa + "\n")

def mostrar_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

tarefas = carregar_tarefas()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        salvar_tarefas(tarefas)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nLista de tarefas:")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. {tarefa}")

    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa para remover.")
        else:
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. {tarefa}")
            try:
                numero = int(input("Digite o número da tarefa para remover: "))
                if 1 <= numero <= len(tarefas):
                    removida = tarefas.pop(numero - 1)
                    salvar_tarefas(tarefas)
                    print(f"Tarefa '{removida}' removida com sucesso!")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Digite um número válido.")

    elif opcao == "4":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
