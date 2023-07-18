#receita bruta x (aliquota) 7,6%


receita_bruta = str(input('Qual a Receita Bruta do mês anterior?  ')).replace('.','').replace(',','.')
custo_prestacao = str(input('Quais são os custos de prestação de serviço do mês anterior?  ')).replace('.','').replace(',','.')
aliquota = 7.6

resultado_1 = float(receita_bruta) * (aliquota/100)
resultado_2 = float(custo_prestacao) * (aliquota/100)
print(f'Calculo da Receita Bruta : R$ {resultado_1:.2f}')
print(f'Calculo dos custos das prestações de serviços: R$ {resultado_2:.2f}')

pis = resultado_1-resultado_2

print(f' O valor correto do Cofins é: R$ {pis:.2f}')

input('Verifique se o valor está igual ao que está na darf ^')