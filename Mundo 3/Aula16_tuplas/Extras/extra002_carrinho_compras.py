carrinho = ()
for produto in range(1, 5):
    valor = float(input("Valor do produto: "))
    carrinho += (valor,)
    if produto == 1:
        caro = valor
        barato = valor
    if valor > caro:
        caro = valor
    if valor < barato:
        barato = valor
texto = ""
for item in carrinho:
    texto += f"R$ {item:.2f}, "
print(f"Valores digitados: {texto.rstrip(' R$, ')}")
print(f"Valor total da compra: R$ {sum(carrinho):.2f}")
print(f"Produto mais caro: R$ {caro:.2f} \nProduto mais barato: R$ {barato:.2f}")