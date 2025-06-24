produtos = []
funcionarios = []
usuarios = {"gui12": 123, "gui123": 1234}

def acesso():
    while True:
        print("Bem vindo ao Login")
        print("Faça seu login")
        login = input("Login: ").strip().lower()

        if login not in usuarios:
            print("Login inexistente, cadastre novo acesso!")
            novo_login = input("Novo Login: ").strip().lower()

            if novo_login in usuarios:
                print("Esse login já existe. Tente outro.")
                continue
            
            try:
                nova_senha = int(input("Nova Senha: "))
                usuarios[novo_login] = nova_senha
                print("Cadastro realizado com sucesso!")
            except ValueError:
                print("A senha deve ser um número!")
        else:
            try:
                senha = int(input("Senha: "))
                if senha == usuarios[login]:
                    print("Acesso permitido")
                    tela_menu()
                else:
                    print("Senha incorreta")
            except ValueError:
                print("A senha deve ser um número!")



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
    

def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        for i, f in enumerate(funcionarios, start=1):
            print(f"{i}. Nome: {f['nome'].title()} | Idade: {f['idade']} | Cargo: {f['cargo'].title()}")

    

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



def tela_menu():
    while True:
        print("===============MENU==============")
        print("Bem vindo o Menu Principal")
        print("1 - Acessar Menu da Gerência \n2 - Cadastrar Produtos \n3 - Atualizar Produtos \n4 - Remover Produtos \n5 - Listar Produtos \n0 - Encerrar \n")

        try:
            opcao = int(input("Escolha uma opção: \n"))
        except ValueError:
            print("Digite um número válido!")
            continue

        if opcao == 1:
            menu_gerente()
        elif opcao == 2:
            cadastro_produtos()
        elif opcao == 3:
            atualizar_produtos()
        elif opcao == 4:
            remover_produtos()
        elif opcao == 5:
            listar_produtos()
        elif opcao == 0:
            print("Programa Encerrado")
            break
        else:
            print("Digite uma opção válida!")
            

def listar_produtos():
    print("Bem-vindo à Lista de Produtos")
    lista_fornecedor = input("Digite o nome do Fornecedor: ").strip()

    encontrados = False  # Flag para saber se encontrou algum

    for i, p in enumerate(produtos, start=1):
        if p["fornecedor"].lower() == lista_fornecedor.lower():
            print(f"{i}. {p['fornecedor']} | {p['nome']} | Quantidade: {p['quantidade']} | Valor unitário: R${p['valor']:.2f}")
            encontrados = True

    if not encontrados:
        print("Nenhum produto encontrado para esse fornecedor.")

def atualizar_produtos():
    print("=== Atualizar Produtos ===")
    nome_produto = input("Digite o nome do produto que deseja atualizar: ").strip().lower()
    fornecedor = input("Digite o nome do fornecedor: ").strip().lower()

    for produto in produtos:
        if produto["nome"] == nome_produto and produto["fornecedor"] == fornecedor:
            print("Produto encontrado!")
            try:
                nova_quantidade = int(input("Digite a nova quantidade: "))
                novo_valor = float(input("Digite o novo valor: "))
                produto["quantidade"] = nova_quantidade
                produto["valor"] = novo_valor
                print("Produto atualizado com sucesso!")
                return
            except ValueError:
                print("Quantidade e valor precisam ser números válidos!")
                return

    print("Produto não encontrado.")


def remover_produtos():
    print("=== Remover Produtos ===")
    nome_produto = input("Digite o nome do produto que deseja remover: ").strip().lower()
    fornecedor = input("Digite o nome do fornecedor: ").strip().lower()

    for i, produto in enumerate(produtos):
        if produto["nome"] == nome_produto and produto["fornecedor"] == fornecedor:
            print(f"Produto encontrado: {produto['nome'].title()} - {produto['fornecedor'].title()}")
            confirmacao = input("Tem certeza que deseja remover? (s/n): ").strip().lower()
            if confirmacao == "s":
                produtos.pop(i)
                print("Produto removido com sucesso!")
                return
            else:
                print("Remoção cancelada.")
                return

    print("Produto não encontrado.")



def cadastro_produtos():
    print("Bem Vindo ao Cadastro de Produtos")
    fornecedor = input("Digite o nome do Fornecedor: \n").strip().lower()
    nome_produto = input("Digite qual produto: \n").strip().lower()

    try:
        quantidade = int(input("Digite a quantidade: \n"))
        valor = float(input("Digite o valor do produto: \n"))
    except ValueError:
        print("Quantidade e valor devem ser números válidos!")
        return

    produto = {
        "nome": nome_produto,
        "fornecedor": fornecedor,
        "quantidade": quantidade,
        "valor": valor
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


acesso()