# Analisador de triângulos 2.0

print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS 2.0')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"Os segmentos acima \033[32mPODEM\033[0m formar um triângulo!")
    if r1 == r2 == r3:
        print("Tipo do triângulo: \033[34mEquilátero")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Tipo do triângulo: \033[34mIsósceles")
    elif r1 != r2 != r3 != r1:
        print("Tipo do triângulo: \033[34mEscaleno\033[0m")
else:
    print("Os segmentos acima \033[31mNÃO PODEM\033[0m formar um triângulo.")
