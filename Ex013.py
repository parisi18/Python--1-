s=float(input('Valor do salário: '))
c1=s+((15/100)*s) #calculo do salário com 15% de aumento
print('Seu novo salário será: \033[4;33m{:.2f}\033[mR$'.format(c1))
