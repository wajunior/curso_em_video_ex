# MEU METODO
frase = str(input('Digite uma frase pra saber se ela é um palíndromo: ')).lower().strip()
nospace = frase.replace(' ', '')
invertida = nospace[::-1]

if invertida == nospace:
    print('A frase {} invertida fica {}'.format(nospace.upper(), invertida.upper()))
    print('A sua frase forma um palíndromo')
else:
    print('A frase {} invertida fica {}'.format(nospace.upper(), invertida.upper()))
    print('Sua frase não forma um palíndromo!')

# MEDOTO DO PROFESSOR COM "FOR"
f = str(input('Digite uma frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase forma um palíndromo!')
else:
    print('A frase não forma um palíndromo!')
