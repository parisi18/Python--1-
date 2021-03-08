vet=[]
while True: #loop inf
    num=vet.append(int(input('Digite um valor: ')))
    opc=str(input('Deseja continuar?'))
    while opc not in 'SsNn': #se digitar errado
        opc = str(input('Deseja continuar?'))
    if opc in 'Nn': #caso queira parar
        break
print(f'Você digitou {len(vet)} elementos') #tamanho do vet
vet.sort(reverse=True) #organiza e reverte
print(f'Os valores em ordem decrescente são {vet}')
if 5 in vet: #se o 5 está na lista
    print('O valor 5 faz parte da lista')
else: #se o 5 não está na lista
    print('O valor 5 não faz parte da lista')
