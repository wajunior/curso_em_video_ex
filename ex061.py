print('Sequencia de fibonacci')
n = int(input('Informe um numero: '))
ultimo = 1
penultimo = 1
cont = 0

print('{} {} {}'.format(0, penultimo, ultimo), end=' ')
while cont < n:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    cont += 1
    print('{}'.format(termo), end=' ')
