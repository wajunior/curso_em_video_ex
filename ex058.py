print('Exercicio fatorial')
num = int(input('Informe o numero para saber o fatorial: '))
mult = 1
n = num

while num >= 1:
    mult *= num
    print('{}'.format(num), end=' x ')
    num -= 1

print('FIM')
print('\n{}! = {}'.format(n, mult))

# Solução simples
from math import factorial
valor = int(input('\nInforme um valor para saber seu fatorial: '))
fat = factorial(valor)
print('{}! = {}'.format(valor, fat))

# método do professor
v = int(input('Informe o numero que deseja fatorar: '))
f = 1
c = v

print('Calculando {}! = '.format(v), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
