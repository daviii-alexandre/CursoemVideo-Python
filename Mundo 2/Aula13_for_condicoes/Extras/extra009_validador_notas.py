from time import sleep
soma = 0
aluno = str(input("Nome do aluno: "))
provas = int(input("Quantidade de provas: "))
for notas_geral in range (1, provas+1):
    nota = float(input("Nota: "))
    soma = soma + nota
media = soma / provas
for repeticao in range(3):
    for pontos in range(4):
        print("\r\033[34mANALISANDO\033[0m" + "\033[34m.\033[0m" * pontos + "  ", end="", flush=True)
        sleep(0.5)
print()
print("-" * 30)
if media >= 7:
    print(f"""\033[1;0mAluno:\033[0m \033[36m{aluno}\033[0m
Status: \033[1;32mAPROVADO\033[0m
Média final: \033[1;35m{media:.1f}\033[0m""")
elif media >= 5:
    print(f"""\033[1;0mAluno:\033[0m {aluno}
Status: \033[1;33mRECUPERAÇÃO - Compareça a diretoria para marcar a SEGUNDA CHAMADA\033[0m
Média final: \033[1;35m{media:.1f}\033[0m""")
else:
    print(f"""\033[1;0mAluno:\033[0m {aluno}
Status: \033[1;31mREPROVADO\033[0m
Média final: \033[1;35m{media:.1f}\033[0m""")
print("-" * 30)
