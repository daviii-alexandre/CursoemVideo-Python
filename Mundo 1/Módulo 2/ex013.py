salario = float(input('Qual o salário do funcionário? R$ '))
aumento = salario * 15 / 100
novo = salario + aumento
print('O funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))