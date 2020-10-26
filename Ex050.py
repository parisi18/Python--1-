soma=0
cont=0
for c in range(1,6): #dentro de uma seq de 5 num
    num=int(input('Digite um número inteiro: '))
    if num%2==0: #se o num fo par
        cont+=1 #conta somente os pares
        soma+=num #soma todos os pares
print('A soma dos {} números pares é igual a {}'.format(cont,soma))