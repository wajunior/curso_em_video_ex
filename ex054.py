maisvelho = ''
maiorI = 0
media = 0
menorM = 0

for c in range(1, 5):
    print('======= {}ª PESSOA ======='.format(c))
    nome = str(input('Nome: ')).upper().strip()
    idd = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    media += idd / 4

    if sexo == 'M':
        if c == 1:
            maisvelho = nome
            maiorI = idd
        else:
            if idd > maiorI:
                maisvelho = nome
                maiorI = idd
    else:
        if idd < 20:
            menorM += 1

print('\n')
print('A média de idade das 4 pessoas é {}'.format(media))
print('O nome do homem mais velho é {} e ele tem {} anos'.format(maisvelho, maiorI))
print('{} pessoa do sexo feminino tem menos de 20 anos'.format(menorM))
