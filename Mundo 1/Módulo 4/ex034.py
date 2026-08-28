# Analisar aumento de salário

salario = float(input('Digite o seu salário: '))
cores = {
    'limpa': '\033[0m',
    'amarelo': '\033[33m',
    'verde': '\033[32m]',
}

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Você ganhava um salário de {cores['amarelo']}R${salario}{cores['limpa']}, agora passa a ganhar um salário de {cores['verde']}R${novo}{cores['limpa']}')