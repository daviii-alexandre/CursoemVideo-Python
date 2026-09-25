print("=" * 40)
print(f"\033[1;33m{'TABELA DE PREÇOS':^40}\033[m")
print("=" * 40)
lista = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
for produtos in range(0, len(lista), 2):
    print(f"{lista[produtos]:.<32}\033[32mR$ {lista[produtos + 1]:>6.2f}\033[m")
print("=" * 40)