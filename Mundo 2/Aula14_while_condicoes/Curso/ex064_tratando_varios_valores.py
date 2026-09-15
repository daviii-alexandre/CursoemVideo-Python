n = int(input("Digite um valor [999 para parar]: "))
soma = 0
cont = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um valor [999 para parar]: "))
print("-" * 30)
print(f"\033[1;32mALELOIAS!!\033[m Eu só queria que você digitasse \033[1;35m999\033[m")
print(f"Você digitou \033[35m{cont}\033[m números, e a soma dos valores das suas tentativas foi \033[36m{soma}\033[m")