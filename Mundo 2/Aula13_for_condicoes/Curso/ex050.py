# Soma do Pares

s = 0
cont = 0
for numeros in range (1, 7):
    escolha = int(input("Digite um número: "))
    if escolha % 2 != 0:
        escolha = 0
        cont += 1
    s += escolha
print(f"A soma dos {cont} é igual a {s}")