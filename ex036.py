n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

if n1 > n2:
    print('O valor {} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('O valor {} é maior que {}'.format(n2, n1))
else:
    print('Os valores {} e {} são iguais!'.format(n1, n2))
