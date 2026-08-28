# Triângulos com Asteriscos

n = int(input("Qual será a altura do triângulo em linhas? "))
triangulo = "*"
for tamanho in range (1, n+1):
    espacos = n - tamanho
    vazio = " " * espacos
    print(vazio + triangulo)
    triangulo += "*"
