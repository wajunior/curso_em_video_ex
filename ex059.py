print('Gerador de PA')
print('-=' * 10)
a1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
t = a1
cont = 1

while cont <= 10:
    print('{} -> '.format(t), end='')
    t += r
    cont += 1
print('FIM')
