while True:
    n = int(input('Informe qual valor gostaria de ver a tabuada: '))
    if n < 0:
        break
    else:
        for c in range(1, 11):
            mult = n * c
            print(f'{n:^2} x {c:^2} = {mult:^2}')
    print('-=' * 30)
print('#' * 30)
print('Programa tabuada encerrado!')
