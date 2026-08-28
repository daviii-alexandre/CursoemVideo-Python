# Números Primos

e_primo = True
n = int(input("Digite um número: "))
for primo in range (2, n):
    if n % primo == 0:
        e_primo = False
if e_primo:
    print("Primo")
else:
    print("Não primo")


'''tot = 0
n = int(input("Digite um número: "))
for primo in range (1, n+1):
    if n % primo == 0:
        print("\033[36m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print(f"{primo} ", end=" ")
print(f"\n\033[mO número \033[32m{n}\033[m foi divisível \033[35m{tot}\033[m vezes")
if tot == 2:
    print("Então ele \033[32mÉ PRIMO\033[m")
else:
    print("Então ele \033[31mNÃO É PRIMO\033[m")'''
