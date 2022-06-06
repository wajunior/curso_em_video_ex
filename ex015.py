from math import hypot

catO = float(input('Digite o valor do cateto oposto: '))
catA = float(input('Digite o valor do cateto adjacente: '))
hypo = hypot(catO, catA)

print('O valor da Hypotenusa é: {:.2f}'.format(hypo))
