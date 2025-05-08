from cliente import cadastrar_cliente, listar_clientes
from cardapio import adicionar_produto, listar_produtos

while True:
    print("\n--- MENU DELÍCIAS DA DONA MARIA ---")
    print("1. Cadastrar cliente")
    print("2. Adicionar produto ao cardápio")
    print("3. Ver clientes")
    print("4. Ver cardápio")
    print("5. Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        telefone = input("Telefone: ")
        cadastrar_cliente(nome, telefone)
    elif opcao == "2":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: ").replace(",", "."))
        adicionar_produto(nome, preco)
    elif opcao == "3":
        listar_clientes()
    elif opcao == "4":
        listar_produtos()
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")
