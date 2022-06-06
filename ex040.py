l1 = float(input('Informe o valor do primeiro lado: '))
l2 = float(input('Informe o valor do segundo lado: '))
l3 = float(input('Informe o valor do terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print('Triângulo equilatero!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Triângulo isósceles!')
    else:
        print('Triângulo escaleno!')
else:
    print('Os valores não foram um triângulo.')
