from time import sleep
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezzoito', 'dezenove', 'vinte')

while True:
    n = int(input('Informe um numero entre 0 e 20: '))

    while n < 0 or n > 20:
        print('Tente novamente. ', end='')
        n = int(input('Informe um numero entre 0 e 20: '))

    print(f'Valor digitado foi {numeros[n]}')

    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    while cont not in 'SN':
        print('Informe uma opção válida. ', end='')
        cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if cont == 'N':
        break

print('Saindo do programa...')
sleep(1.2)
print('Programa finalizado.')
