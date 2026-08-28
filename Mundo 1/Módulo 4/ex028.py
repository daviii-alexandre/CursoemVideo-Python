# Mini Akinator de números

import random
from time import sleep
numero = random.randint(1, 5)
pergunta = int(input('Vamos lá. Em qual número eu estou pensando? '))
print('PROCESSANDO...')
sleep(2)
if pergunta == numero:
    print('VOCÊ ACERTOU, MEUS PARABÉNS!!! O número que eu pensei realmente foi o {}'.format(numero))
else:
    print('HAHAHA, VOCÊ ERROU!! O número correto era {}'.format(numero))