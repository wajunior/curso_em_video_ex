# meu metodo
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Informe o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} numeros pares e a soma deles é {}'.format(cont, soma))
