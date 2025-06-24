from dados import produtos, funcionarios, usuarios

funcionarios = []

def menu_gerente():
    while True: 
        print("==============MENU GERENCIA===============")
        print("Bem vindo ao Menu da Gerência.")
        print("1 - Cadastro de Funcionario \n2 - Atualizar Cadastro \n3 - Remover Cadastro \n4 - Listar Funcionarios Cadastrados \n5 - Voltar ao Menu Principal \n0 - Encerrar Programa")
        opcao = int(input("Escolha uma opção: \n"))
        

        if opcao == 1:
            cadastro_fun()
        elif opcao == 2:
            atualizar_cadastro()
        elif opcao == 3:
            remover_cadastro()
        elif opcao == 4:
            listar_funcionarios()
        elif opcao == 5:
            break
        elif opcao == 0:
            print("Programa Encerrado")
            exit()
        else:
            print("Digite uma opçao válida!")


def cadastro_fun():
    print("Bem vindo ao Cadastro de Funcionarios")
    nome_funcionario = input("Digite o nome completo: \n").strip().lower()
    idade_funcionario = int(input("Digite a idade: \n"))
    cargo_funcionario = input("Digite o Cargo: \n").strip().lower()
    funcionario = {
        "nome": nome_funcionario,
        "idade": idade_funcionario,
        "cargo": cargo_funcionario
        }
    funcionarios.append(funcionario)
    print("Funcionario Cadastrado com sucesso")

def atualizar_cadastro():
    print("============ Atualizar Cadastro de Funcionário ============")
    nome_funcionario = input("Digite o nome do funcionário que deseja atualizar: ").strip().lower()

    for funcionario in funcionarios:
        if funcionario["nome"] == nome_funcionario:
            print("Funcionário encontrado!")
            try:
                nova_idade = int(input("Digite a nova idade: "))
                novo_cargo = input("Digite o novo cargo: ").strip().lower()
                funcionario["idade"] = nova_idade
                funcionario["cargo"] = novo_cargo
                print("Cadastro atualizado com sucesso!")
                return
            except ValueError:
                print("Idade deve ser um número válido!")
                return

    print("Funcionário não encontrado.")


def remover_cadastro():
    print("============ Remover Cadastro de Funcionário ===============")
    nome_funcionario = input("Digite o nome do funcionário que deseja remover: ").strip().lower()

    for i, funcionario in enumerate(funcionarios):
        if funcionario["nome"] == nome_funcionario:
            print(f"{i+1}. Nome: {funcionario['nome'].title()} | Idade: {funcionario['idade']} | Cargo: {funcionario['cargo'].title()}")
            confirmacao = input("Tem certeza que deseja remover? (s/n): ").strip().lower()
            if confirmacao == "s":
                funcionarios.pop(i)
                print("Funcionário removido com sucesso!")
                return
            else:
                print("Remoção cancelada.")
                return

    print("Funcionário não encontrado.")


def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        for i, f in enumerate(funcionarios, start=1):
            print(f"{i}. Nome: {f['nome'].title()} | Idade: {f['idade']} | Cargo: {f['cargo'].title()}")
