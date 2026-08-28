# Separando dígitos de um número

numero = int(input('Digite um número: '))
num = str(numero)
print('Analisando o número {}, por favor aguarde.'.format(numero))

print('Milhar: {}'.format(num[0]))
print('Centena: {}'.format(num[1]))
print('Dezena: {}'.format(num[2]))
print('Unidade: {}'.format(num[3]))