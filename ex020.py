nome = str(input('Informe seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maíusculo é: ', nome.upper())  # nome em maiúsculo
print('Seu nome em minúsculo é: ', nome.lower())  # nome em minúsculo
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ', ''))))  # substitui os espaços vazios juntando as palavras e informando a quantidade de as
# letras
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # substitui os espaços vazios juntando as palavras e informando a quantidade de as
# letras
div = nome.split()  # transforma o nome em uma lista
print('Seu primeiro nome {} tem ao todo {} letras'.format(div[0], len(div[0])))  # mostra a quantas letras tem no primeiro nome
