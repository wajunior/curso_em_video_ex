casa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe o seu salário bruto: R$ '))
prestacao = int(input('Informe em quantos anos pretende pagar: '))

valorprestacao = casa / (prestacao * 12)
negado = (salario * 30 / 100)

if valorprestacao >= negado:
    print('Desculpe, o valor da prestação de R$ {:.2f} compromete 30% do seu salário (R$ {:.2f}).\n'
          'O compra será negada!'.format(valorprestacao, negado))
else:
    print('Parbéns, compra aprovada!\n'
          'Valor da casa: R$ {:.2f}\n'
          'Parcelamento em {}x\n'
          'Valor da mensalidade: R$ {:.2f}'.format(casa, prestacao * 12, valorprestacao))
