from math import hypot
#calcular o valor da hipotenusa
s=float(input('Digite o cateto adjascente: '))
s2=float(input('Digite o cateto oposto: '))
hi=hypot(s,s2)
#mostrar a hipotenusa
print('O valor da hipotenusa é \033[4;34m{:.2f}\033[m'.format(hi))
