# Alistamento Militar Obrigatório

from datetime import date
nome = str(input('Nome Completo: ')).strip().title()
atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento
print('''\033[35mIndicação de sexo\033[0m
[ 1 ] Masculino
[ 2 ] Feminino''')
sexo = int(input('Sexo: '))
limpo = '\033[0m'
vermelho = '\033[1;31m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
if sexo == 1:
    if idade < 18:
        print(f"Informamos que {nome} {azul}ainda não está na idade certa{limpo} para participar do alistamento militar obrigatório.")
        print(f"{amarelo}Faltam {18 - idade} anos{limpo} para você se alistar")
    elif idade == 18:
        print(f'informamos que {nome} {amarelo}já está na idade{limpo} para participar do alistamento militar obrigatório.')
    else:
        print(f'Informamos que {nome} {vermelho}já passou da idade{limpo} para participar do alistamento militar obrigatório.')
        print(f"Você deveria ter se alistado há {vermelho}{idade - 18} anos")
elif sexo == 2:
    print(f"Você {vermelho}NÃO PRECISA{limpo} participar do alistamento militar obrigatório.")