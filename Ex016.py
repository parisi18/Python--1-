#usando a função trunc dentro do .format
'''from math import trunc #importar trunc da biblioteca math

s=float(input('Digite um número real qualquer: ')) # pedir para digitar

# mostrar o número inteiro arredondando para baixo
print('O número {} tem a parte inteira {}'.format(s,trunc(s)))'''

#ou usando a função int dentro do .format

num=float(input('Digite um valor: '))
print('O valor digitado foi \033[1;33m{}\033[m e a sua porção inteira é \033[1;34m{}\033[m'.format(num, int(num)))
