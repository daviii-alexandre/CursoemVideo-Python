from time import sleep
print("-" * 30)
print("LOJÃO BANANYAS")
print("-" * 30)
soma = 0
cont = 0
mais_mil = 0
barato = ""
menor = 0
while True:
    nome = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$ "))
    soma += preco
    cont += 1
    if preco >= 1000:
        mais_mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    pergunta = " "
    while pergunta not in "SN":
        pergunta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if pergunta == "N":
        break
print("=" * 30)
print("Calculando...")
print("=" * 30)
sleep(1)
print(f"""Valor Total: R$ {soma:.2f}
Produtos acima de R$ 1000,00: {mais_mil}
Produto mais barato: {barato} (R$ {menor:.2f})""")