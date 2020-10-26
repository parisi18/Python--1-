from random import randint
from time import sleep
pc=randint(0,10)
cont=1
print(pc)
print('Vou pensar em um número de 0 - 10!')
jog=int(input('Qual número você acha que é?: '))
if jog == pc and cont == 1: #se acertou de primeira
    print('Parabéns, você acertou de primeira!')
while jog != pc: #enquanto não acerto
    cont += 1 #vai somando as tentativas
    jog = int(input('Qual número você acha que é?: '))
    if jog>pc: #se o valor jogado foi maior
        print('hmmm')
        sleep(1)
        print('Acho que não.. MENOS')
    elif jog<pc: #se for menor
        print('hmmm')
        sleep(1)
        print('Acho que não... MAIS')
    if jog==pc and cont!=1: #se acertou mas não de primeira
        print('Você acertou! mas precisou de {} tentativas'.format(cont))