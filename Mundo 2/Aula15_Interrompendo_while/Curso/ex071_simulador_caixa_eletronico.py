print("=" * 30)
print("\033[1;30;43mBANCO BAN\033[m".center(40))
print("=" * 30)
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_1 = 0
valor = int(input("Qual valor deseja sacar? R$ "))
while True:
    notas_50 = valor // 50
    valor = valor % 50
    notas_20 = valor // 20
    valor = valor % 20
    notas_10 = valor // 10
    valor = valor % 10
    notas_1 = valor // 1
    valor = valor % 1
    break
print("=" * 30)
print(f"""Total de cédulas de R$50,00: {notas_50}
Total de cédulas de R$20,00: {notas_20}
Total de cédulas de R$10,00: {notas_10}
Total de cédulas de R$1,00: {notas_1}""")
print("=" * 30)
print("""O \033[1;33mBANCO BAN\033[m agradece a sua preferência.
\033[1;32mTENHA UM BOM DIA! 😊\033[m""")