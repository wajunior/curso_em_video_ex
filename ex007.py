n1 = int(input('Digite um numero inteiro: '))
i = 0
cont = 0

print('A tabuada de {}'.format(n1))

for i in range(10):
    cont = cont + 1
    print('{} x {:2} = {}'.format(n1, cont, n1*cont))
