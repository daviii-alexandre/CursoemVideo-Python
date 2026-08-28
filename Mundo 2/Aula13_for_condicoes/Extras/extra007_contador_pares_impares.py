# Contador de Pares e Ímpares

pares = 0
impares = 0
for contagem in range(1, 6):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Pares: \033[1;36m{pares}\033[0m")
print(f"Ímpares: \033[35m{impares}\033[0m")

# 32, 4, 25, 19, 3