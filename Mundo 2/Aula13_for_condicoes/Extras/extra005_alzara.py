# Jogo de adivinhação com tentativas limitadas

from random import randint
pc = randint(1, 10)
print("\033[36mALZARA JR.\033[0m")
print(('-' * 20))
for usuario in range (3):
    chute = int(input("Advinha qual número estou pensando: "))
    if chute == pc:
        print("\033[1;32mPARABÉNS!! Você adivinhou o meu número!\033[00m")
        print(('-' * 20))
        break
    elif chute > pc:
        print("Um pouco \033[1;35mpra baixo\033[0m...")
        print(('-' * 20))
    else:
        print("Chuta um pouco mais \033[1;33mpra cima\033[0m...")
        print(('-' * 20))
if chute != pc:
    print(f"\033[1;31mGAME OVER!!!\033[0m O número era \033[1;34m{pc}\033[0m")