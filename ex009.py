a = float(input('Qual a largura da parede: '))
l = float(input('Qual a altura da parede: '))
m = a * l

print('Parede é {} x {}\n'
      'Total {:.2f}m²\n'
      'Você precisa de {:.1f} litros de tintas'.format(a, l, m, m/2))