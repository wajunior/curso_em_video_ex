import random

nome1 = input('Digite o nome do aluno 1: ')
nome2 = input('Digite o nome do aluno 2: ')
nome3 = input('Difite o nome do aluno 3: ')
nome4 = input('Digire o nome do aluno 4: ')

lista = [nome1, nome2, nome3, nome4]

rdn = random.choice(lista)

print('O aluno sorteado para apagar o quadro foi {}'.format(rdn))
