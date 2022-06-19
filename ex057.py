from time import sleep
# meu metodo
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

# metodo do professor
num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
opção = 0

while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior valor
    [4] Novos numeros
    [5] Sair do programa''')
    opção = int(input('>>>>>> Opção desejada: '))

    if opção == 1:
        soma = num1 + num2
        print('A soma de {} + {} = {}'.format(num1, num2, soma))
    elif opção == 2:
        prod = num1 * num2
        print('A multiplicação entre {} x {} = {}'.format(num1, num2, prod))
    elif opção == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o maior valor é {}'.format(num1, num2, maior))
    elif opção == 4:
        print('Informe novos valores!')
        num1 = int(input('Informe o primeiro valor: '))
        num2 = int(input('Informe o segundo valor: '))
    elif opção == 5:
        print('Finalizando!')
    else:
        print('Opção incorreta, tente novamente!')
    print('-=-' * 10)

sleep(2)
print('Volte sempre!')