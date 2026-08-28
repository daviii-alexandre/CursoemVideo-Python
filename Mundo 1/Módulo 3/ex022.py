# Analisador de Textos

nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separado = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separado [0], len(separado[0])))

