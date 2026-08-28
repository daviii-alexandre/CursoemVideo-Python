# Soma de Números Primos

soma = 0
n = int(input("Digite o número limite: "))
for numeros in range (1, n):
    e_primo = True
    if numeros == 1:
        e_primo = False
    for primos in range (2, numeros):
        if numeros % primos == 0:
            e_primo = False
    if e_primo:
        soma += numeros
print(soma)