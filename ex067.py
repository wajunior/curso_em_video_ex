qtdM = qtdF = iddT = 0
print('-' * 50)
print('{:^50}'.format('CADASTRE UMA PESSOA'))
print('-' * 50)
while True:
    idade = int(input('Informe a idade: '))

    sexo = ' '
    while sexo not in 'mM' or sexo not in 'fF':
        sexo = str(input('Informe o sexo: [M/F] ')).upper().strip()[0]
        if sexo in 'mM' or sexo in 'fF':
            break

    if sexo in 'mM':
        qtdM += 1
    elif sexo in 'Ff':
        if idade < 20:
            qtdF += 1

    cont = ' '
    while cont not in 'sS' or cont not in 'nN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if cont in 'Nn' or cont in 'Ss':
            break

    if cont in 'nN':
        break

    if idade > 18:
        iddT += 1

print(f'Quantidade de pessoas com mais de 18 anos: {iddT}')
print(f'Quantidade de homens cadastrados: {qtdM}')
print(f'Quantidade de mulheres com menos de 20 anos: {qtdF}')
