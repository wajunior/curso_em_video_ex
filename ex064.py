soma = 0
qtd = 0

while True:
    num = int(input('Informe um valor (999 para sair): '))

    if num == 999:
        break
    soma += num
    qtd += 1
print(f'Você informou {qtd} numeros e a soma foi {soma}')
