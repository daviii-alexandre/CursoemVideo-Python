soma = 0
numero = int(input("Número limite: "))
for contagem in range(1, numero+1):
    if contagem % 3 == 0:
        soma = soma + contagem
print(f"A soma dos números múltiplos de 3 até {numero} é {soma}")