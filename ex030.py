from datetime import date
ano = int(input('Informe o ano para saber se ele é bissexto ou não! Coloque 0 para analisar ano atual: '))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('O ano de {} é Bissexto!'.format(ano))
else:
    print('O ano de {} não é Bissexto!'.format(ano))