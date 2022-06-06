# meu método
a1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
n = 10
pa = a1 + (n - 1) * r
pos = 0

for c in range(a1, pa+1, r):
    pos += 1
    print('{:^3}º Termo: {:^3}'.format(pos, c))
