km = int(input('Informe a distância da viagem: '))

if km <= 200:
    valor = km * 0.50
    print('A viagem tem: {} Km\n'
          'Valor a ser cobrado: R$ {:.2f}'.format(km, valor))
else:
    valor = km * 0.45
    print('A viagem tem: {} Km\n'
          'Valor a ser cobrado: R$ {:.2f}'.format(km, valor))
