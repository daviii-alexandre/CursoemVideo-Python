print("-" * 30)
print("CADASTRE UMA PESSOA")
print("-"* 30)
mulher = 0
maior_idade = 0
homens = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    if idade >= 18:
        maior_idade += 1
    if idade >= 20 and sexo == "F":
        mulher += 1
    if sexo == "M":
        homens += 1
    mensagem = " "
    while mensagem not in "SN":
        mensagem = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    print("-" * 35)
    if mensagem == "N":
        break
print("======= FIM DO PROGRAMA =======")
print(f"""Total de pessoas com mais de 18 anos: {maior_idade}
Total de HOMENS cadastrados: {homens}
Total de MULHERES com mais de 20 ANOS: {mulher}""")