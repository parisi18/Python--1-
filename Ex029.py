inf=float(input('Qual a velocidade atual de seu carro? => '))
if inf > 80:
    s=(inf-80)*7 # ver os quilometros adicionais e multar
    print('ACIMA DA VELOCIDADE!! MULTADO NO VALOR DE \033[4m{:.2f}R$\033[m'.format(s))
else:
    print('Dentro da velocidade, DRIVE SAFE')
