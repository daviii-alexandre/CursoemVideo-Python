# Comparando Números

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O \033[34mprimeiro número\033[0m é \033[32mmaior\033[0m.')
elif n1 < n2:
    print('O \033[34msegundo número\033[0m é \033[32mmaior\033[0m.')
else:
    print('\033[1;31mNão existe\033[0m valor maior, os dois são \033[35miguais\033[0m')