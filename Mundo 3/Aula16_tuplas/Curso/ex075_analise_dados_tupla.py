pares = ""
num = (int(input("Digite um número: ")),
       int(input("Digite um número: ")),
       int(input("Digite um número: ")),
       int(input("Digite um número: ")))
numeros = (f"Você digitou os valores: {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3) + 1}ª posição")
else:
    print("O valor 3 não foi digitado")
for n in num:
    if n % 2 == 0:
        print("Os valores pares digitados foram: ", end="")
        print(n, end=" ")
    else:
        print("Nenhum valor par foi digitado")
        break