print('Esse e meu primeiro git copiado ks')
class Tarefa:
    def __init__(self):
        self.titulo = input("Digite o nome da tarefa: ")
    
loop = -1
tarefas = []
while loop != 0:
    print("Bem-vindo ao Programa de Gerenciamento de Tarefas!")
    print("Opções Disponíveis:")
    print("1 - Adicionar uma nova tarefa")
    print("2 - Exibir a lista de tarefas pendentes")
    print("3 - Sair do programa\n\n")
    
    opcao = int(input("Digite o número correspondente à opção desejada: "))
    if opcao == 1:
        print("Adicionar uma nova tarefa\n")
        tarefas.append(Tarefa())
        print("\n")
    elif opcao == 2:
        print("Exibir a lista de tarefas pendentes\n")
        for tarefa in tarefas:
            print(tarefa.titulo)
        print("\n")
    elif opcao == 3:
        print("Encerrando o programa...\n")
        loop = 0
    else:
        print("Opção inválida. Tente novamente.")
