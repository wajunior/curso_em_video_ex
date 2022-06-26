times = ('Palmeiras', 'Corinthians', 'Internacional', 'Athletico-PR', 'Atlético-MG', 'Santos', 'São Paulo',
         'Bragantino', 'Avaí', 'América-MG', 'Ceará', 'Fluminense', 'Flamengo', 'Coritiba', 'Botafogo', 'Goiás',
         'Atlético-GO', 'Cuiabá', 'Juventude', 'Fortaleza')

print('-=-' * 10)
print(f'A lista dos times brasileiro é: {times}')
print('-=-' * 10)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-=-' * 10)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=-' * 10)
print(f'Os times em ordem alfabética é: {sorted(times)}')
print('-=-' * 10)
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição')
