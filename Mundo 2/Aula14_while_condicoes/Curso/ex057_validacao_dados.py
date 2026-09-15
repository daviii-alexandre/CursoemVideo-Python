sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input("\033[1;31mDADOS INVÁLIDOS\033[m. Por favor, informe seu sexo: ")).strip().upper()[0]
if sexo == 'M':
    print(f"Sexo \033[34mM (masculino)\033[m registrado com sucesso")
else:
    print(f"Sexo \033[35mF (feminino)\033[m registrado com sucesso")