vdd = 1
s = ''
while vdd != 0:
    sexo = str(input('Informe o sexo da pessoa [M/F]: ')).upper()

    if sexo == 'M' or sexo == 'F':
        vdd = 0
        if sexo == 'M':
            s = 'MASCULINO'
        else:
            s = 'FEMININO'
    else:
        print('Valor incorreto, informe novamente!')

print('O sexo informado foi {}'.format(s))