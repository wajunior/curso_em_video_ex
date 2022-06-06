import math

num = float(input('Digite o valor de um ângulo: '))
seno = math.sin(math.radians(num))
cosseno = math.cos(math.radians(num))
tang = math.tan(math.radians(num))

print('O valor do ângulo digitado foi: {}\n'
      'Seno do ângulo: {:.2f}\n'
      'Conseno do ângulo: {:.2f}\n'
      'Tangente do ângulo: {:.2f}'.format(num, seno, cosseno, tang))
