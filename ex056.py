from random import randint
comp = randint(0, 10)

print('Tente adivinhar no numero que estou pensando entre 0 e 10')

# meu método
n = int(input('Informe um numero: '))
t = 1
while comp != n:
    t += 1
    if n < comp:
        n = int(input('Mais... informe novo numero:  '))
    else:
        n = int(input('Menos... informe novo nuemro: '))

print('Parabêns vc acertou, o numero foi {} e vc precisou de {} tentativas'.format(comp, t))

# metodo do professor
pc = randint(0, 10)
print('\nSou seu computador... estou pensando em um numero entre 0 e 10!')
print('Consegue acertar?')
palpites = 0
acertou = False

while not acertou:
    num = int(input('Qual é seu palpite? '))
    palpites += 1
    if num == pc:
        acertou = True
    else:
        if num < pc:
            print('Maior... Tente novamente.')
        else:
            print('Menor... Tente novamente.')

print('Parabéns\n'
      'Acertou com {} tentativas'.format(palpites))
