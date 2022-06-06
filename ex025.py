nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
last = n.pop()

print('Nome completo: ', nome)
print('Primeiro nome: ', n[0])
print('Úiltimo nome: ', last)
