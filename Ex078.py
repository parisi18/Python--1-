lista=[]
maior=menor=0
for c in range(0,5): #determino 5 inputs
    lista.append(int(input(f'Digite um valor para a posição {c}:')))
    if c==0: #o primeiro recebe maior e menor
        maior=menor=lista[c]
    else:
        if lista[c]>maior: #se maior q o maior
            maior=lista[c]
        if lista[c]<menor: #se menor q o menor
            menor=lista[c]
print(f'O {maior} está nas posições:',end='')
for i,v in enumerate(lista): #enumera
    if v==maior: #se for o maior
        print(f'{i}...',end='') #mostra a posição
print()
print(f'O {menor} está nas posições:',end='')
for i, v in enumerate(lista):
    if v==menor:
        print(f'{i}...',end='')

