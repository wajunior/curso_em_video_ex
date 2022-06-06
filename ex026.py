import random
from time import sleep # importa a biblioteca sleep

print('-=-' * 27)
print('Jogo de adivinhação, consegue adivinhar qual número o computador pensou?')
print('-=-' * 27)

num = int(input('Informe um numero entre 0 e 5: '))
rdn = random.randint(0, 5)

print('PROCESSANDO...')
sleep(2) # faz o processamento do programa aguardar 2 seg antes de continuar

print('Número do computador foi: {}'.format(rdn))

if num == rdn:
    print('Parabêns, você venceu!')
else:
    print('Sinto muito, o computador vencêu!')
