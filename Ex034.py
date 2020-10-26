s=int(input('Qual o valor do salário?: '))
if s>1250:
    print('O aumento será de {:.2f}R$'.format((1.10*s)-s))
else:
    print('O aumento será de {:.2f}R$'.format((1.15*s)-s))
