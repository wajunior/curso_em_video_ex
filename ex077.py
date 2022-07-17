lista = []
while True:
    p = int(input('Digite um valor: '))

    if p in lista:
        print('Valores duplicados! Não será adicionado.')
    else:
        lista.append(p)
        print('Valor adicionado com sucesso...')

    cont = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

    while cont not in 'SN':
        print('Opção inválida!')
        cont = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break

print('-=' * 30)
print(f'Sua lista contem os valores: {sorted(lista)}')
