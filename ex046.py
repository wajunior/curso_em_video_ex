# meu metodo
soma = 0
num = 0

for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
        num += 1
print('A soma de todos os {} valores ímpares multiplos de 3 entre 1 e 500 é {}'.format(num, soma))

# metodo do professor
s = 0
n = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        n += 1
print('A soma de todos os {} valores ímpares multiplos de 3 entre 1 e 500 é {}'.format(n, s))
