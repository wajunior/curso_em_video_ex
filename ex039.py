# categoria atleta
from datetime import date
ano = int(input('Informe o ano de nascimento do atleta: '))
idade = date.today().year - ano

print('Idade: {}\n'.format(idade))
print('Categoria:')

if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTÍL')
elif 14 < idade <= 19:
    print('JÚNIOR')
elif 19 < idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')