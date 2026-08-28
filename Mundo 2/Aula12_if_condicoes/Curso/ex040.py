# Analise de média escolar

from time import sleep
nome = str(input('Digite o nome do aluno: ')).strip().title()
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('-' * 30)
print(f"Analisando situação do(a) aluno(a): \033[1;36m{nome}\033[0m...")
sleep(2)
print('\033[32mANÁLISE CONCLUÍDA\033[0m')
if media < 5.0:
    print(f"Situação do(a) aluno(a): \033[1;31mREPROVADO\033[0m.")
elif media < 7.0:
    print(f"Situação do(a) aluno(a): \033[1;33mRECUPERAÇÃO (Encaminhe-se até seu professor e solicite a 2 chamada)\033[0m")
else:
    print(f"Situação do(a) aluno(a): \033[1;32mAPROVADO\033[0m")
