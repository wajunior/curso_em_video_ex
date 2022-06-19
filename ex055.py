# meu metodo
vdd = 1
s = ''
while vdd != 0:
    sexo = str(input('Informe o sexo da pessoa [M/F]: ')).upper().strip()

    if sexo == 'M' or sexo == 'F':
        vdd = 0
        if sexo == 'M':
            s = 'MASCULINO'
        else:
            s = 'FEMININO'
    else:
        print('Valor incorreto, informe novamente!')

print('Sexo {} registrado com sucesso'.format(s))

# metodo do professor

s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]  # pega apenas a primeira letra
while s not in 'MF':
    s = str(input('Dados inválidos! Por favor informe seu sexo:  ')).strip().upper()[0]  # pega apenas a primeira letra
print('Sexo {} registrado com sucesso!'.format(s))
