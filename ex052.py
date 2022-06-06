from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    anonasc = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c)))
    if atual - anonasc >= 21:
        maior += 1
    elif atual - anonasc < 21:
        menor += 1
print('{} são maiores de idade\n'
      '{} são menores de idade'.format(maior, menor))
