preco = totalgasto = menor = maior = c = 0
nomeMenor = ''

print('-' * 50)
print('{:^50}'.format(' HIPERMERCADO SÓ VEM'))
print('-' * 50)

while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço do produto: R$ '))
    cont = ' '

    totalgasto += preco

    if preco >= 1000:
        maior += 1

    if c == 0:
        menor = preco
        nomeMenor = nome
    else:
        if preco < menor:
            menor = preco
            nomeMenor = nome
    c += 1

    while cont not in 'Ss' or cont not in 'Nn':
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if cont in 'sS' or cont in 'nN':
            break
    if cont in 'nN':
        break

print('=' * 50)
print(f'Total da compra = R$ {totalgasto:.2f}\n'
      f'Quantidade de produtos com valor maior que R$ 1000,00: {maior}\n'
      f'O produto mais barato foi {nomeMenor} e custou {menor:.2f}')
