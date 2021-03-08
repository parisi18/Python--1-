lst=[]
while True: #quantos inputs quiser
    s=int(input('Digite um número: '))
    if s in lst: #se já está na lista
        print('Numero duplicado...')
    else: #caso contrario adicione o numero na lista
        lst.append(s)
    opc = str(input('Deseja continuar? [S/N]')) #deseja continuar?
    while opc not in 'SsNn': #se digitar errado
        opc = str(input('Deseja continuar? [S/N]'))
    if opc in 'Nn': #caso não queira continuar
        break
print(sorted(lst)) #mostra a lista ordenada