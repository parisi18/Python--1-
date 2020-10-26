num=c=soma=0 #variaveis iniciam do 0
num=int(input('Digite um valor[999 para parar]: '))
while num!=999: #enquanto não digitar 999
    soma+=num #soma os numeros
    c+=1 #contador soma mais um
    num = int(input('Digite um valor[999 para parar]: '))
print('Você digitou {} números e a soma é {}'.format(c,soma))