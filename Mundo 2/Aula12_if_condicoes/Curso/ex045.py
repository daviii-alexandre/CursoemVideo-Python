# Jokenpô

import random
from time import sleep
print("+"*30)
print("1 = Pedra")
print("2 = Papel")
print("3 = Tesoura")
print("+"*30)
escolha = int(input("Escolhe aí vai... "))
pc = random.choice([1, 2, 3])
print("\033[1;36mJO...\033[0m")
sleep(1)
print("\033[1;36mKEN...\033[0m")
sleep(1)
print("\033[1;36mPÔ\033[0m")
if escolha == 1 and pc == 1 or escolha == 2 and pc == 2 or escolha == 3 and pc == 3:
    print(f"\033[33mDeu EMPATE!!")
elif escolha == 1 and pc == 2:
    print(f"Você escolheu \033[35mPEDRA\033[0m e eu escolhi \033[34mPAPEL\033[0m, então parece que \033[31mVOCÊ PERDEU!\033[0m")
elif escolha == 1 and pc == 3:
    print(f"Você escolheu \033[35mPEDRA\033[0m e eu escolhi \033[34mTESOURA\033[0m, então parece que \033[32mVOCÊ ME VENCEU!!!\033[0m")
elif escolha == 2 and pc == 1:
    print(f"Você escolheu \033[35mPAPEL\033[0m e eu escolhi \033[34mPEDRA\033[0m, então parece que \033[32mVOCÊ ME VENCEU!!!\033[0m")
elif escolha == 2 and pc == 3:
    print(f"Você escolheu \033[35mPAPEL\033[0m e eu escolhi \033[34mTESOURA\033[0m, então parece que \033[31mVOCÊ PERDEU!\033[0m")
elif escolha == 3 and pc == 1:
    print(f"Você escolheu \033[35mTESOURA\033[0m e eu escolhi \033[34mPEDRA\033[0m, então parece que \033[31mVOCÊ PERDEU!\033[0m")
elif escolha == 3 and pc == 2:
    print(f"Você escolheu \033[35mTESOURA\033[0m e eu escolhi \033[34mPAPEL\033[0m, então parece que \033VOCÊ ME VENCEU!!!\033[0m")
elif escolha < 1 or escolha > 3:
    print("Oxi, doidão. Coloca um número certo aí poh!")