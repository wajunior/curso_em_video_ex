frase = str(input('Digite uma frase: ')).strip()

print('Frase tem {} caracteres "A"'.format(frase.lower().count('a')))
print('A letra "A" aparece pela primeira vez na posição: {}'.format(frase.lower().find('a')+1))
print('A letra "A" aparece pela última vez na posição: {}'.format(frase.lower().rfind('a')+1))  # mostra a última posição da
# palavra ou letra encontrada pelo FIND
