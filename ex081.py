parenteses = list(str(input("Informe uma expressão matemática: ")))
checagem_ini = []
checagem_fin = []
for i in parenteses:
    if i == '(':
        checagem_ini.append(i)
    if i == ')':
        checagem_fin.append(i)

if len(checagem_ini) == len(checagem_fin):
    print('Sua expressão é válida!')
else:
    print('Sua expressão está incorreta!')

##########################################
# método do professor

expr = str(input('Informe uma expressão matemática: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
