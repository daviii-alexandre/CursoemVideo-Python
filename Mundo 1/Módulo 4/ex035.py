# Analisando um triângulo

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print(f'Os segmentos acima {'\033[1;32m'}PODEM{'\033[0m'} formar um triângulo!')
else:
    print(f'Os segmentos acima {'\033[1;31m'}NÃO PODEM{'\033[0m'} formar um triângulo!')