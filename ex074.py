produtos = ('Pão', 10.00,
            'Leite', 5.20,
            'Arroz', 22.80,
            'Óleo', 7.60,
            'Feijão', 6.30,
            'Áçucar', 3.40,
            'Café', 12.10,
            'Salcicha', 18.00,
            'Coxão mole', 32.00,
            'Coxa de frango', 7.70,
            'Bisteca suína', 23.12,
            'Carne moída de 2ª', 28.00,
            'Carne moída de 1ª', 45.00)

print('-' * 39)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 39)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>3.2f}')
print('-' * 39)
