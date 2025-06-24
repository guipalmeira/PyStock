from menu_gerencia import menu_gerente


produtos = []

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