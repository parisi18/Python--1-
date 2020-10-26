from random import randint
v=0
while True:
    jog=int(input('Diga um valor: '))
    pc=randint(0,10) #ALEATORIO EM 0-10
    total=jog+pc #TOTAL
    tipo=str(input('Par ou impar? [P/I]')).strip().upper()[0] #ESCOLHER PAR OU IMPAR
    while tipo not in 'PI': #SE N ESCOLHER CERTO
        tipo = str(input('Par ou impar? [P/I]')).strip().upper()[0] #REPETE
    print(f'Você jogou {jog} e o computador jogou {pc}. Total de {total}') #MOSTRAR A JOGADA
    print('DEU PAR' if total%2==0 else 'DEU IMPAR') #MOSTRAR A JOGADA
    if tipo=='P': #CONDIÇÃO PAR
        if total %2==0:
            print('Você venceu')
            v+=1
        else:
            print('Você perdeu')
            break
    elif tipo=='I': #CONDIÇÃO DE IMPAR
        if total%2!=0:
            print('Você venceu')
        else:
            print('Você perdeu')
            break