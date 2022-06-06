km = float(input('Km percorrido do carro: '))
dias = int(input('Quantidade de dias alugados: '))
diaria = dias * 60
kmr = km * 0.15
total = kmr + diaria

print('Km percorrido: {:.2f} KM\n'
      'Dias alugado: {}\n'
      'Valor total da diária: R$ {:.2f}\n'
      'Valor total do KM rodado: R$ {:.2f}\n'
      'O valor total a pagar é R$ {:.2f}'.format(km, dias, diaria, kmr, total))
