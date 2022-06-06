from random import choice
from time import sleep

print('-=-' * 20)
print('{:^60}'.format(' JOKENPÔ'))
print('-=-' * 20)

print('=' * 60)
print('Escolha entre:\n'
      'PEDRA - PAPEL - TEROUSA\n\n'
      'PEDRA ganha de TESOURA\n'
      'TESOURA ganha de PAPEL\n'
      'PAPEL ganha de PEDRA.')
print('=' * 60)

comp = choice(['Pedra', 'Papel', 'Tesoura']).lower()
player = str(input('Escolha sua opção: ')).lower()

if player == 'pedra' or player == 'papel' or player == 'tesoura':
    print('\nJO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('PO!!!')
    print('=' * 60)

    if comp == player:
        print('Deu impate!')
        print('Computador escolheu: {}\n'
              'Player escolheu: {}'.format(comp.upper(), player.upper()))

    elif comp == 'pedra' and player == 'tesoura':
        print('Computador Venceu!')
        print('Computador escolheu: {}\n'
              'Player escolheu: {}'.format(comp.upper(), player.upper()))

    elif comp == 'tesoura' and player == 'papel':
        print('Computador Venceu!')
        print('Computador escolheu: {}\n'
              'Player escolheu: {}'.format(comp.upper(), player.upper()))

    elif comp == 'papel' and player == 'pedra':
        print('Computador Venceu!')
        print('Computador escolheu: {}\n'
              'Player escolheu: {}'.format(comp.upper(), player.upper()))

    if player == 'pedra' and comp == 'tesoura':
        print('Player Venceu!')
        print('Computador escolheu: {}\n'
              'Player escolheu: {}'.format(comp.upper(), player.upper()))

    elif player == 'tesoura' and comp == 'papel':
        print('Player Venceu!')
        print('Computador escolheu: {}\n'
              'Player escolheu: {}'.format(comp.upper(), player.upper()))

    elif player == 'papel' and comp == 'pedra':
        print('Player Venceu!')
        print('Computador escolheu: {}\n'
              'Player escolheu: {}'.format(comp.upper(), player.upper()))

else:
    print('Opção inválida!')
