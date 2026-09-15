from random import randint
tentativas = 1
print("------ ALZARA v2.0 ------")
pc = randint(1, 10)
acertou = False
while not acertou:
    user = int(input("Em qual número de 1 a 10 eu estou pensando? "))
    if user == pc:
        acertou = True
    else:
        if user < pc:
            print("\033[36mMais...\033[m Tenta de novo")
        elif user > pc:
            print("\033[35mMenos...\033[m Tente de novo")
        tentativas += 1
print('-' * 30)
print(f"""\033[1;32mPARABÉNS!\033[m O número que eu pensei foi exatamente o \033[35m{pc}\033[m
\033[36mNúmero de Tentativas:\033[m {tentativas}""")