vel = int(input('Informe a velocidade do carro: '))
limite = 80

if vel <= limite:
    print('Tenha um bom dia, siga com segurança!')
else:
    velmax = vel - limite
    multa = (vel - limite) * 7
    print('Você estava {}km/h acima da velodiade limite de 80km/h\n'
          'Sua multa é de R$ {}'.format(velmax, multa))