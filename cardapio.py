produtos = []

def adicionar_produto(nome, preco):
    produtos.append({"nome": nome, "preco": preco})

def listar_produtos():
    for produto in produtos:
        print(f"{produto['nome']} - R$ {produto['preco']:.2f}")
