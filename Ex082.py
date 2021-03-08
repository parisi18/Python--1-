vet=[]
veti=[]
vetp=[]
while True: #loop inf
    num=int(input('Digite um valor: '))
    vet.append(num) #adiciona todos na vet completa
    if num%2==0: #se for par
        vetp.append(num)
    else: #se for ímpar
        veti.append(num)
    opc=str(input('Deseja continuar?'))
    while opc not in 'SsNn': #se digitar errado
        opc = str(input('Deseja continuar?'))
    if opc in 'Nn': #caso queira parar
        break
print(f'A lista completa é {vet}') #vet completa
print(f'A lista de pares é {vetp}') #pares
print(f'A lista de ímpares é {veti}') #ímpares
