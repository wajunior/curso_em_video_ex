c = 1
soma = 0
total = 0

print('Digite 999 para sair!')
while c != 0:
    num = int(input('Informe um valor: '))
    if num != 999:
        total += c
        soma += num
    else:
        c = 0
print('Você informou {} numeros'.format(total))
print('E a soma deles foi {}'.format(soma))
