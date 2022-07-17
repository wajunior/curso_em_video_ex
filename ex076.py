lista = []
maior = []
menor = []
for l in range(0, 5):
    lista.append(int(input(f'Informe um valor para a posição {l}: ')))

print('-=' * 30)
print(f'Sua lista contem os valores {lista}')

for p, v in enumerate(lista):
    if v == max(lista):
        maior.append(p)
    if v == min(lista):
        menor.append(p)

print(f'O maior valor foi {max(lista)} na posição {maior}')
print(f'O menor valor foi {min(lista)} na posição {menor}')
############################################################
# método do professor

listanum = []
mai = men = 0

for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('-=' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()

print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()
