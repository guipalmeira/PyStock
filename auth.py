from menu import tela_menu


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