lista_completa = []
lista_pares = []
lista_impar = []

while True:
    num = int(input('Digite um numero: '))
    lista_completa.append(num)

    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    while cont not in 'SN':
        print('Opção incorreta! ', end='')
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if cont == 'N':
        break

for i in lista_completa:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impar.append(i)

print('='* 30)
print(f'A lista completa é: {lista_completa}\n'
      f'Lista só com números pares: {lista_pares}\n'
      f'Lista só com números ímpares: {lista_impar}')

