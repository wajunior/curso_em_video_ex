print('{:=^40}'.format(' LOJAS JUNIORS '))
produto = float(input('Informe o valor do produto: R$ '))
pagamento = int(input('Informe a forma de pagamento:\n'
                      '[1] - À vista no dinheiro/cheque.\n'
                      '[2] - À vista no cartão.\n'
                      '[3] - Parcelado.\n'
                      ': '))
if pagamento == 1:
    valor = produto * 10 / 100
    print('Valor do produto: R$ {:.2f}\n'
          'Desconto por forma de pagamento: 10%\n'
          'Valor do desconto: R$ {:.2f}\n'
          'Valor a pagar: R$ {:.2f}'.format(produto, valor, produto - valor))
elif pagamento == 2:
    valor = produto * 5 / 100
    print('Valor do produto: R$ {:.2f}\n'
          'Desconto por forma de pagamento: 5%\n'
          'Valor do desconto: R$ {:.2f}\n'
          'Valor a pagar: R$ {:.2f}'.format(produto, valor, produto - valor))
elif pagamento == 3:
    parcelamento = int(input('Informe quantas vezes gostaria de parcelar: '))
    if parcelamento == 2:
        print('Valor do produto: R$ {:.2f}\n'
              'Quantidades de parcelas: {}\n'
              'valor das parcelas: R$ {:.2f}\n'
              'Valor total do produto: R$ {:.2f}'.format(produto, parcelamento, produto / parcelamento, ((produto / parcelamento) * parcelamento)))
    elif parcelamento > 2:
        valor = produto * 20 / 100
        total = produto + valor
        print('Valor do produto: R$ {:.2f}\n'
              'Acréscimo de juros: 20%\n'
              'Valor do Juros: R$ {:.2f}\n'
              'Valor da parcela: {:.2f}\n'
              'Valor a pagar: R$ {:.2f}'.format(produto, valor, total / parcelamento, (total / parcelamento) * parcelamento))
else:
    print('Opção inválida!')
