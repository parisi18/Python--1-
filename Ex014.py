s=float(input('Informe a temperatura em Cº: '))
s2=(s*(9/5)+32)#calculo de Fahrenheit
print('A temperatura de \033[0;31m{:.2f}\033[mCº corresponde a \033[0;34m{:.1f}\033[mºF '.format(s,s2))