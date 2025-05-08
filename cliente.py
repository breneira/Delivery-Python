clientes = []

def cadastrar_cliente(nome, telefone):
    clientes.append({"nome": nome, "telefone": telefone})

def listar_clientes():
    for cliente in clientes:
        print(f"Nome: {cliente['nome']} - Tel: {cliente['telefone']}")
