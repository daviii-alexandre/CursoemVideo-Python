from time import sleep
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
for repeticao in range(3):
    for pontos in range(4):
        print("\r\033[1;36mCarregando Menu de Opções\033[m" + "\033[36m.\033[m" * pontos + "  ", end="", flush=True)
        sleep(0.3)
print("")
print("-" * 30)
menu = ("""\033[35mMENU DE OPÇÕES
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números 
[ 5 ] Sair\033[m""")
print(menu)
print("-" * 30)
escolha = int(input("Escolha: "))
while escolha != 5:
    if escolha == 1:
        soma = n1 + n2
        print(f"\033[36mSoma: {n1} + {n2} = {soma}\033[m")
        print("-" * 30)
        print(menu)
    elif escolha == 2:
        multi = n1 * n2
        print(f"\033[36mMultiplicação: {n1} * {n2} = {multi}\033[m")
        print("-" * 30)
        print(menu)
    elif escolha == 3:
        if n1 > n2:
            maior = n1 
            print(f"O maior número é \033[36m{maior}\033[m")
            print("-" * 30)
            print(menu)
        else:
            maior = n2
            print(f"O maior número é \033[36m{maior}\033[m")
            print("-" * 30)
            print(menu)
    elif escolha == 4:
        n1 = int(input("Digite um novo valor: "))
        n2 = int(input("Digite outro novo valor: "))
        print("-" * 30)
        print(menu)
        print("-" * 30)
    elif escolha == 5:
        print("\033[36mSAINDO\033[m")
        sleep(1)
        print("\033[1;32mPROCESSO FINALIZADO\033[m")
    else:
        print("\033[1;31mOpção Inválida\033[m")
    print("-" * 30)
    escolha = int(input("Escolha: "))
print("Fim do programa! Volte sempre!")