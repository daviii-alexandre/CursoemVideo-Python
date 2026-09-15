numero = int(input("Digite um número: "))       # Pede o número ao usuário
texto = ""      # Variável para guardar o texto do fatorial
cont = numero
atual = 1
while cont >= 1:
    atual *= cont
    texto += f"{cont} x "
    cont -= 1
print(f"Calculando {numero}! = {texto.rstrip(' x ')} = {atual}")