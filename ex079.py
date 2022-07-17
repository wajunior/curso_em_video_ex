lista = []
c = 0

while True:
    num = int(input('Informe um valor: '))
    lista.append(num)
    c += 1

    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    while cont not in 'SN':
        print('Valor inválido! ', end='')
        cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break

lista.sort(reverse=True)

print('-=' * 30)
print(f'Foram informados {c} valores!')
print(f'A lista em ordem decrescente fica: {lista}')
if 5 in lista:
    print(f'O valor 5 foi encontrado na lista na posição {lista.index(5)}')
else:
    print('O valor 5 não foi encontrado na lista.')

#################################################

# método do professor
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]: '))

    if r in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} valores')
valores.sort(reverse=True)
print(f'Sua lista de forma decrescente fica {valores}')
if 5 in valores:
    print('O valor 5 foi encontrado na lista')
else:
    print('O valor 5 não foi encontrado na lista')
