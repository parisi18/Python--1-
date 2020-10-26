qtd=0
num=int(input('Digite um número inteiro: ' ))

for c in range(1,num+1): #numa sequencia de 1 até input+1
    if num%c==0: #se for divisível pela posição da sequência
        qtd +=1 #soma +1, mostrando a qtd de numeros divididos
        print('\033[33m', end='')
    else: #caso contrario ele não é divisível
        print('\033[31m',end='')
    print(c,end=' ')
if qtd == 2: #se o numero de divisões foi 2 ele é primo
    print('\033[m\nO número {} foi dividido {}x\nPor isso É PRIMO'.format(num,qtd))
else: #caso contrário ele não é primo
    print('\033[mO número {} foi dividido {}x\nPor isso NÃO é PRIMO'.format(num,qtd))