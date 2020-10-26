soma = 0
cont = 0
for c in range (1,501): #nessa qntd de numeros
    if c%2!=0 and c%3==0: #n ser divisivel por 2 e divisivel por 3
        cont += 1 #o numero 0 + os numeros do laço
        soma += c #a soma de todos os numeros do laço
print('A soma de todos os {} valores é {}'.format(cont,soma))
