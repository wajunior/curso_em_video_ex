palavras = ('python', 'exercicio', 'maquiagem', 'cachorro', 'preguiça', 'batman', 'legiao',
            'macarrao', 'festa', 'cerveja', 'televisao', 'mercado', 'videogame')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
