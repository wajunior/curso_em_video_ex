c = 1

while c != 0:
    n1 = int(input('Informe o 1º valor: '))
    n2 = int(input('Informe o 2º valor: '))
    n = 1

    while n != 0:
        print('=' * 50)
        print('Escolha uma das opções\n'
              '[1] - Somar\n'
              '[2] - Multiplicar\n'
              '[3] - Ver o maior valor\n'
              '[4] - Informar novos valores\n'
              '[5] - Sair')
        opc = int(input('Escolha a opção: '))

        if opc == 1:
            soma = n1 + n2
            print('{} + {} = {}'.format(n1, n2, soma))
        elif opc == 2:
            mult = n1 * n2
            print('{} x {} = {}'.format(n1, n2, mult))
        elif opc == 3:
            if n1 > n2:
                print('O maior numero digitado foi {}'.format(n1))
            else:
                print('O maior numero digitado foi {}'.format(n2))
        elif opc == 4:
            n = 0
        elif opc == 5:
            n = 0
            c = 0
        else:
            print('Opção incorreta!')

print('Saindo do programa')
