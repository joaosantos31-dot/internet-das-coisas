import os
os.system("cls")
tarefas = []
while True:
    os.system("cls")
    print("=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Mostrar tarefas")
    print("0 - Sair")
    print("==============================")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        os.system("cls")
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa)
        print("\nTarefa adicionada com sucesso!")
        input("\nPressione Enter para continuar...")
    elif opcao == '2':
        os.system("cls")
        if not tarefas:
            print("A lista de tarefas está vazia!")
        else:
            print("--- Tarefas Atuais ---")
            for idx, item in enumerate(tarefas, start=1):
                print(f"{idx}. {item}")
            print("----------------------")
            tarefa_remover = input("\nDigite exatamente o nome da tarefa que deseja remover: ")
            if tarefa_remover in tarefas:
                tarefas.remove(tarefa_remover)
                print("\nTarefa removida com sucesso!")
            else:
                print("\nTarefa não encontrada na lista!")
        input("\nPressione Enter para continuar...")
    elif opcao == '3':
        os.system("cls")
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("--- Sua Lista de Tarefas ---")
            for idx, item in enumerate(tarefas, start=1):
                print(f"{idx}. {item}")
        input("\nPressione Enter para continuar...")
    elif opcao == '0':
        os.system("cls")
        print("Programa encerrado!")
        break
    else:
        print("\nOpção inválida!")
        input("\nPressione Enter para continuar...")