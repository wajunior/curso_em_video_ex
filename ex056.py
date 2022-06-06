from random import randint
comp = randint(0, 10)
c = 1
total = 0
print('Tente adivinhar no numero que estou pensando entre 0 e 10')

while c != 0:
    num = int(input('Informe um valor: '))
    if num == comp:
        c = 0
        print('Parabêns você venceu!\n'
              '{} foi o numero escolhido'.format(comp))
    else:
        print('Que pena, não foi o numero escolhido\n'
              'Tente novamente!')
        total += 1

print('Você precisou de {} tentativas para acertar o numero escolhido'.format(total))