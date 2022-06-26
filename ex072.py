from random import randint

# meu método
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = 0
menor = 10

print(f'Numeros sorteados: ', end='')
for c in numeros:
    print(f'{c}', end=' ')

    if c > maior:
        maior = c
    if c < menor:
        menor = c

print(f'\nO maior número digitado foi {maior}\n'
      f'O menor número digitado foi {menor}')

######################################################
# metodo do professor

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Numeros sorteados: ', end='')
for x in n:
    print(f'{x}', end=' ')
print(f'\nO maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')
