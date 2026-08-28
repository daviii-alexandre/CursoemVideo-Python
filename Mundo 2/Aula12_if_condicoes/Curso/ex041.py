# Analise de categoria de natação

from datetime import date
ano = int(input('Digite o ano de nascimento do(a) atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print("Categoria do(a) atleta: \033[36mMIRIM\033[0m")
elif idade > 9 and idade < 14:
    print("Categoria do(a) atleta: \033[35mINFANTIL\033[0m")
elif idade > 14 and idade <= 19:
    print("Categoria do(a) atleta: \033[32mJUNIOR\033[0m")
elif idade == 20:
    print("Categoria do(a) atleta: \033[33mSÊNIOR\033[0m")
else:
    print("Categoria do(a) atleta: \033[31mMASTER\033[0m")