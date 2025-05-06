# calculadora_pedidos.py

# Cardápio de produtos
cardapio = {
    1: {"nome": "Coxinha", "preco": 5.00},
    2: {"nome": "Brigadeiro", "preco": 2.50},
    3: {"nome": "Bolo de Morango", "preco": 20.00}
}

# Total do pedido
total = 0.0

print("--- CARDÁPIO DELÍCIAS DA DONA MARIA ---")
for codigo, item in cardapio.items():
    print(f"{codigo}. {item['nome']} - R$ {item['preco']:.2f}")
print("4. Encerra pedido")

# Loop de pedidos
while True:
    try:
        escolha = int(input("\nDigite o número do produto: "))
        if escolha == 4:
            break
        elif escolha in cardapio:
            qtd = int(input(f"Quantos '{cardapio[escolha]['nome']}'? "))
            subtotal = qtd * cardapio[escolha]["preco"]
            total += subtotal
            print(f"Produto adicionado: {cardapio[escolha]['nome']} x{qtd} = R$ {subtotal:.2f}")
        else:
            print("Produto inválido.")
    except ValueError:
        print("Entrada inválida. Tente novamente com números.")

# Resultado final
print(f"\n🧾 Valor total do pedido: R$ {total:.2f}")
