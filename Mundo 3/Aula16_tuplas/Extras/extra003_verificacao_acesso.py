convidados = ("LUCAS", "FAGNER", "LETICIA", "BRYAN", "CARLOS", "VITORIA")
nome = str(input("Nome: ")).upper()
if nome in convidados:
    print(f"Olá, {nome}! Seja bem-vindo!")
else:
    print(f"Perdão, {nome}, mas seu nome não está na lista de convidados.")