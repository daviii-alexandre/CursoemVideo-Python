# Medidor de velocidade + Multa

velo = float(input('Qual foi a velocidade do veículo? '))
multa = (velo - 80) * 7
if velo > 80:
    print("-----------------------------")
    print('Verificamos que o seu veículo passou pelo nosso radar a {}Km/h, ultrapassando o limite de velocidade da via.\nComo consequência, receberá uma multa no valor de R${:.2f}.'.format(velo, multa))
    print("-----------------------------")