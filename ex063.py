# meu metodo
cont = 1
maior = menor = media = c = 0

while cont != 0:
    num = int(input('Informe o valor: '))
    r = str(input('Gostaria e continuar: ')).lower()
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

print('Você digitou {} numeros\n'
      'A média dos valores informados foi {:.2f}'.format(c, media / c))
print('O maior numero informado foi {}\n'
      'O menor numero informado foi {}'.format(maior, menor))

# método do professor
resp = 'S'
soma = qtd = m = ma = me = 0
while resp in 'Ss':
    n = int(input('Informe um valor: '))
    soma += n
    qtd += 1

    if qtd == 1:
        ma = me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
m = soma / qtd
print('Você digitou {} números\n'
      'A soma entre eles foi {}\n'
      'A média entre eles é {:.2f}'.format(qtd, soma, m))
print('O maior número digitado foi {}\n'
      'O menor número digitado foi {}'.format(ma, me))
