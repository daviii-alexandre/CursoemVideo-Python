distancia = float(input('Qual foi a distância percorrida? '))
passagem1 = distancia * 0.50
passagem2 = distancia * 0.45
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia < 200:
    print('Valor total da viagem: {:.2f}'.format(passagem1))
else:
    print('Valor total da viagem: {:.2f}'.format(passagem2))