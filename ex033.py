# Informar o valor de 3 retas para verificar se formam um triangulo
r1 = float(input('Informe o valor da primeira reta: '))
r2 = float(input('Informe o valor da segunda reta: '))
r3 = float(input('Informe o valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os valores foram um triangulo')
else:
    print('Os valores não foram um triangulo')