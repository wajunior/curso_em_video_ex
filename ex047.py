num = int(input('Informe o numero que gostaria de ver a tabuada: '))

print('A tabuada de {}'.format(num))

for c in range(1, 11):
    print('{:^3} x {:^3} = {:^3}'.format(num, c, num * c))
