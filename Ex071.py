valor=int(input('Qual valor deseja sacar?: '))
total=valor #atribuo a uma nova variavel
ced=50 #inicio com cel 50
totced=0 #contador inicia no 0
while True:
    if total>=ced: #se o valor total for maior que 50
        total-=ced #vai descontando 50
        totced+=1 #conta as cedulas de 50
    else: #quando chegar no valor de 50
        if totced>0: #se for maior que 0
            print(f'O total de {totced} cédulas de {ced}') #printa a qtd e as cedulas
        if ced==50: #quando chegar em 50
            ced=20 #vira 20
        elif ced==20:#chegou em 20
            ced=10#vira 10
        elif ced==10:#chegou em 10
            ced=1#vira 1
        totced=0#quando chegar no final
        if total==0:
            break #para