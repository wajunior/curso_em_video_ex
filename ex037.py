# alistamento
from datetime import date
sexo = str(input('Informe seu sexo\n'
                 '[M] - MASCULINO\n'
                 '[F] - FEMININO\n'
                 ': ')).lower()
if sexo == 'f':
    print('Para mulher o alistamento não é obrigatório!')

elif sexo == 'm':
    print('Alistamento obrigatório!\n')
    anonasci = int(input('Informe seu ano de nascimento: '))
    hoje = date.today().year
    idade = hoje - anonasci

    print('Quem nasceu em {} tem {} anos'.format(anonasci, idade))
    if idade < 18:
        saldo = 18 - idade
        print('Não é hora de se alistar.\n'
              'Faltam {} anos para o seu alistamento!'.format(saldo))
        print('Seu alistamento será em {}'.format(hoje + saldo))
    elif idade == 18:
        print('Favor comparecer a junta militar mais próxima com seus documentos pessoais.')
    else:
        saldo = idade - 18
        print('Você ja passou do seu tempo de alistamento.\n'
          '{} anos de atraso'.format(saldo))
    print('Seu alistamento foi em {}'.format(hoje - saldo))
else:
    print('Opção inválida!')