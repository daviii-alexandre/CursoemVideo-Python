# Conversor de Bases Numéricas

num = int(input("Digite um núumero inteiro: "))
print('''Escolha uma das bases de conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opção = int(input("Sua opção: "))
if opção == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif opção == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif opção == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print('OPÇÃO INVÁLIDA')
