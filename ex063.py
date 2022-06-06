cont = 1
maior = 0
menor = 0
media = 0
c = 0

while cont != 0:
    num = int(input('Informe o valor: '))
    r = str(input('Gostaria e continuar: ')).lower()
    cont += 1
    c += 1
    media += num

    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    if r != 's':
        cont = 0

print('A média dos valores informados foi {:.2f}'.format(media / c))
print('O maior numero informado foi {}\n'
      'O menor numero informado foi {}'.format(maior, menor))
