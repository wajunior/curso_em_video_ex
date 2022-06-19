from random import randint
qtd = soma = 0
while True:
    comp = randint(0, 10)
    valor = int(input('Informe um valor: '))
    soma = comp + valor
    op = ' '

    while op not in 'PI':
        op = str(input('Par ou Impar: [P/I] ')).upper().strip()[0]

    if op == 'P':

        if soma % 2 == 0:
            print('Você venceu!')
            print(f'Computador escolheu {comp} e você escolheu {valor}, a soma foi {soma}. "PAR"')
            qtd += 1
        else:
            print('Computador venceu')
            print(f'Computador escolheu {comp} e você escolheu {valor}, a soma foi {soma}. "IMPAR"')
            break
    elif op == 'I':

        if soma % 2 != 0:
            print('Você venceu!')
            print(f'Computador escolheu {comp} e você escolheu {valor}, a soma foi {soma}. "IMPAR"')
            qtd += 1
        else:
            print('Computador venceu!')
            print(f'Você escolheu {valor} e o computador escolheu {comp}, a soma é {soma}. "PAR"')
            break
    else:
        print()

print(f'GAME OVER! Você venceu {qtd} vezes!')
