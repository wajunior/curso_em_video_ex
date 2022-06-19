# meu método
print('=' * 50)
print('{:^50}'.format('BANCO WAJUNIOR'))
print('=' * 50)

print('Notas no valor de\n'
      'R$ 50,00\n'
      'R$ 20,00\n'
      'R$ 10,00\n'
      'R$ 1,00')
print('=' * 50)

valor = int(input('Qual valor deseja sacar: R$ '))
cinquenta = vinte = dez = um = 0

while valor >= 50:
    cinquenta += 1
    valor -= 50

while valor >= 20:
    vinte += 1
    valor -= 20

while valor >= 10:
    dez += 1
    valor -= 10

while valor >= 1:
    um += 1
    valor -= 1

print('=' * 50)
print(f'Serão entregues:\n'
      f'{cinquenta:^2} notas de R$ 50,00\n'
      f'{vinte:^2} notas de R$ 20,00\n'
      f'{dez:^2} notas de R$ 10,00\n'
      f'{um:^2} notas de R$ 1,00')
print('=' * 50)
print('Obrigado, volte sempre!')

# método do professor
'''print('=' * 50)
print('{:^50}'.format('BANCO WAJUNIOR'))
print('=' * 50)
real = int(input('Qual valor deseja sacar: R$ '))
total = real
ced = 50
totalced = 0

print('=' * 50)
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R$ {ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 50)
print('VOLTE SEMPRE! Obrigado.')'''
