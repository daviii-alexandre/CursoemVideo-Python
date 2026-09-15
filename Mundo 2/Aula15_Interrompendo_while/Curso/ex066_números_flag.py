from time import sleep
soma = 0
cont = 0
while True:
    n = int(input("Digite um valor (999 para parar): "))
    if n == 999:
        break
    soma += n
    cont += 1
print("\033[1;34mCalculando...\033[m")
sleep(1)
print("-" * 40)
print(f"A \033[35mSOMA\033[m dos \033[35m{cont}\033[m valores é igual a \033[35m{soma}\033[m")
print("-" * 40)