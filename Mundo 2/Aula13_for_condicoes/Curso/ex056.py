e_homi = False
soma = 0
homi_idoso = ""
muie_pequena = 0
for nomes in range(1, 5):
    print(f"----- {nomes}ª PESSOA -----")
    nome = str(input("Nome: ")).strip().title()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M/F): ")).upper().strip()
    soma = idade + soma
    if sexo == "M":
        if e_homi == False:
            homi_idoso = nome
            idade_idoso = idade
            e_homi = True
        elif idade > idade_idoso:
            homi_idoso = nome
            idade_idoso = idade
    elif sexo == "F":
        if idade < 20:
            muie_pequena += 1
media = soma / 4
print(f"A \033[1;34mMÉDIA DE IDADE\033[0m do grupo é de \033[34m{media} anos\033[0m")
print(f"O \033[1;33mHOMEM MAIS VELHO\033[0m se chama: \033[2;31m{homi_idoso}\033[0m")
print(f"Exatamente \033[35m{muie_pequena}\033[0m mulheres estão \033[1;35mABAIXO DE 20 ANOS\033[0m")
