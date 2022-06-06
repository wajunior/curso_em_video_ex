num = str(input('Digite um numero de 0 a 9999: '))

if len(num) == 1:
    print('Unidade: {}'.format(num))
elif len(num) == 2:
    print('Unidade: {}'.format(num[1]))
    print('Dezena: {}'.format(num[0]))
elif len(num) == 3:
    print('Unidade: {}'.format(num[2]))
    print('Dezena: {}'.format(num[1]))
    print('Centena: {}'.format(num[0]))
else:
    print('Unidade: {}'.format(num[3]))
    print('Dezena: {}'.format(num[2]))
    print('Centena: {}'.format(num[1]))
    print('Milhar: {}'.format(num[0]))
    