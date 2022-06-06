a1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
n = 0
c = 0

while c < 10:
    n += a1 * r
    print('{}'.format(n), end='->')
    c += 1
print('FIM')
