produto = float(input('Qual o valor do produto? R$'))
desc = produto - (produto * 5 / 100)
print('O produto que custava {:.2f} agora passará a custar R${:.2f} devido ao desconto de 5%.'.format(produto, desc))