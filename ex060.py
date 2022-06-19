print('Gerador de PA')
print('-=' * 10)
a1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
t = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(t), end='')
        t += r
        cont += 1

    print('PAUSA')
    mais = int(input('Informe quantos termos a mais gostaria de verificar: '))
print('FIM')
print('Foram mostrados {} termos'.format(total))

