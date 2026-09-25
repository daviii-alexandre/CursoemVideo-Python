from time import sleep

f_cadastrados = ()

while True:
    cadastro = str(input("Deseja cadastrar um funcionário? [S/N] ")).upper()
    if cadastro != "":
        cadastro = cadastro[0]

    if cadastro == "S":
        nome = str(input("Nome do Funcionário: "))
        f_cadastrados += (nome,)
    elif cadastro == "N":
        print("-" * 30)
        print("Encerrando Cadastramento de Funcionários...")
        sleep(1.5)
        print("\033[1;31mCADASTRAMENTO ENCERRADO\033[m")
        print("-" * 30)

        if f_cadastrados == ():
            print("\033[1;33mNenhum funcionário foi cadastrado.\033[m")
        else:
            print(f"Funcionários cadastrados: {f_cadastrados}")

        print(f"Quantidade de funcionários cadastrados: \033[32m{len(f_cadastrados)}\033[m")

        if f_cadastrados == ():
            print()
        else:
            print(f"Último funcionário cadastrado: \033[35m{f_cadastrados[-1]}\033[m")
        break
    else:
        print("\033[31mVALOR INVÁLIDO!\033[m")