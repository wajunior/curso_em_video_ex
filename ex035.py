num = int(input('Informe um número: '))
converter = int(input('Informe para qual base você gostaria de converter!\n'
                      '[1] - binário.\n'
                      '[2] - octal.\n'
                      '[3] - hexadecimal.\n'
                      ': '))
if converter == 1:
    print('Número digitado: {}\n'
          'Binário: {}'.format(num, format(num, 'b')))
elif converter == 2:
    print('Número digitado: {}\n'
          'Octal: {}'.format(num, format(num, 'o')))
elif converter == 3:
    print('Número digitado: {}\n'
          'Hexadecimal: {}'.format(num, format(num, 'x').upper()))
else:
    print('Opção incorreta!')
