lista=[]
for c in range(0,5): #em uma sequencia de 5
    n=int(input('Digite um número: ')) #dados do input
    if c==0 or n>lista[-1]: #se for o primeiro ou maior que o ultimo
        lista.append(n) #adicionar na lista
    else:
        pos=0 #contador
        while pos<len(lista):#enqt o contador for menor q o tamanho da lista
            if n<= lista[pos]: #se o input for menor ou igual que a lista na pos
                lista.insert(pos,n) #vou inserir na posição o n
                break #finaliza
            pos+=1 #soma +1
print(lista)


