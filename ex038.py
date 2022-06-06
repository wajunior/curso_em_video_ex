nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('Nota 1: {:.1f}\n'
          'Nota 2: {:.1f}\n'
          'Média: {:.1f}\n'
          'Reprovado!'.format(nota1, nota2, media))
elif 5 < media < 7:
    print('Nota 1: {:.1f}\n'
          'Nota 2: {:.1f}\n'
          'Média: {:.1f}\n'
          'Recuperação!'.format(nota1, nota2, media))
else:
    print('Nota 1: {:.1f}\n'
          'Nota 2: {:.1f}\n'
          'Média: {:.1f}\n'
          'Aprovado!'.format(nota1, nota2, media))
