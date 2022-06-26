n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
n3 = int(input('Informe o terceiro valor: '))
n4 = int(input('Informe o quarto valor: '))

tupla = (n1, n2, n3, n4)
t = ()

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O valor 3 está na {tupla.index(3) + 1}º posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')

print('Os valores pares digitados são: ', end='')
for x in tupla:
    if x % 2 == 0:
        print(x, end=' ')

print('\n')

######################################
# método do professor
num = (int(input('Informe um valor: ')),
       int(input('Informe outro valor: ')),
       int(input('Informe mais um valor: ')),
       int(input('Informe o último valor: ')))

print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O valor 3 está na {num.index(3) + 1}º posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')

print('Os valores pares digitados são: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')

print('\n')
