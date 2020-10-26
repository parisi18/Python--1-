num=int(input('Digite um numero para calcular o fatorial: '))
cont=num
f=1
while cont>0: #se contador for maior q 0
    print('{}'.format(cont),end='') #print a contagem
    print('x' if cont>1 else '=',end='') #coloca x entre os numeros e = no final
    f*=cont #vai criar a multiplicação do fatorial
    cont -= 1 #vai diminuindo a contagem
print('O fatorial de {} é {}'.format(num,f))
