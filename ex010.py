val = float(input('Digite o valor do produto: R$ '))
desc = val - (val * 5 / 100)

print('O valor do produto com 5% de desconto é R$ {:.2f}'.format(desc))
