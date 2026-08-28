# Soma ímpares múltiplos de três

s = 0
cont = 0
for numeros in range (0, 501):
    n = numeros
    if n % 3 == 0 and n % 2 != 0:
        cont += 1
        s += n
print(f"A \033[33mSOMA\033[0m de todos os {cont} \033[36mNÚMEROS ÍMPARES\033[0m e \033[36mMÚLTIPLOS DE 3\033[0m entre 1 e 500 \033[1;31m{s}")
