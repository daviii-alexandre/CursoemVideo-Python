from random import randint
print("---------- VAMOS JOGAR PAR OU ÍMPAR ----------")
vitoria = 0
while True:
    usuario = int(input("Diga um valor: "))
    pc = randint(0, 11)
    total = usuario + pc
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    print("-" * 30)
    print(f"Você jogou {usuario} e o computador {pc}. Total de {total}... ", end="")
    print("\033[36mDEU PAR\033[m" if total % 2 == 0 else "\033[33mDEU IMPAR\033[m")
    print("-" * 30)
    if tipo == "P":
        if total % 2 == 0:
            print("Você \033[32mVENCEU!!!\033[m")
            vitoria += 1
        else:
            print("Você \033[31mPERDEU!\033[m")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você \033[32mVENCEU!!!\033[m")
            vitoria += 1
        else:
            print("Você \033[31mPERDEU!!\033[m")
            break
    print("Vamos jogar novamente...")
    print("-" * 30)
print(f"\033[33mGAME OVER!\033[m Você venceu {vitoria} vezes")
