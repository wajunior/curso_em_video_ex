# Meu metodo
num = int(input('Informe um numero para saber se ele é primo: '))
primo = 0

for c in range(num + 1):
    c += 1
    if num % c == 0:
        primo += 1
if primo > 2:
    print('O numero {} foi divisível {}x, portanto ele não é primo!'.format(num, primo))
else:
    print('O numero {} foi divisível {}x portanto ele é primo!'.format(num, primo))

# método do professor
n = int(input('Informe um numero para saber se ele é primo: '))
p = 0
for c in range(1, n +1):
    if n % c == 0:
        print('\033[33m', end='')
        p += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if p == 2:
    print('\n\033[mO numero {} foi divisível {}x portanto ele é primo!'.format(num, primo))
else:
    print('\n\033[mO numero {} foi divisível {}x, portanto ele não é primo!'.format(num, primo))

