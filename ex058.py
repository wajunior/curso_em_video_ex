print('Exercicio fatorial')
num = int(input('Informe o numero para saber o fatorial: '))
mult = 1
n = num

while num >= 1:
    mult *= num
    print('{}'.format(num), end=' x ')
    num -= 1

print('FIM')
print('\n{}! = {}'.format(n, mult))

