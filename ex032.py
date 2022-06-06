sal = float(input('Informe seu salario: R$ '))

if sal > 1250.00:
    aum = sal * 10 / 100
    nsal = sal + aum
    print('Seu antigo salário era de: R$ {:.2f}\n'
          'Você teve um aumento de 10%: R$ {:.2f}\n'
          'Seu novo salario será de: {:.2f}'.format(sal, aum, nsal))
else:
    aum = sal * 15 / 100
    nsal = sal + aum
    print('Seu antigo salário era de: R$ {:.2f}\n'
          'Você teve um aumento de 15%: R$ {:.2f}\n'
          'Seu novo salario será de: {:.2f}'.format(sal, aum, nsal))
