from math import sin, cos, tan, radians
#importar as funções da biblioteca
s=float(input('Digite um ângulo qualquer: '))
s2=radians(s)
#printar os valores
print('O valor do seno é \033[1;36m{:.2f}\033[m \nDo cosseno é \033[1;34m{:.2f}\033[m \nDa tangente é \033[1;31m{:.2f}\033[m'.format(sin(s2),cos(s2),tan(s2)))

