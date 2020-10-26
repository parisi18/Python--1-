'condição de existencia do triangulo'
'a +b >c  a+c>b  c+b > a'
from time import sleep
print('Digite os lados de um triângulo qualquer: ')
a1=int(input('Lado a: '))
b1=int(input('Lado b: '))
c1=int(input('Lado c: '))

if c1<a1+b1 and b1<a1+c1 and a1<b1+c1:
    print('Esses segmentos podem formar um',end=' ')
    if c1!=a1!=b1!=c1:
        print('triângulo escaleno')
    elif c1==a1==b1:
        print('triângulo equilátero')
    else:
        print('triângulo isósceles')
else:
    print('Esses segmentos NÃO formam triângulo')