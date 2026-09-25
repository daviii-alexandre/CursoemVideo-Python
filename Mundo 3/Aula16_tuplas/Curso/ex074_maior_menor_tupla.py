from random import randint
maior = 1
menor = 1
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("Os números sorteados foram: ", end="")
for num in numeros:
    print(f"{num}", end=" ")
print(f"\nO maior valor sorteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")
