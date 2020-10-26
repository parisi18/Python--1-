from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0,2)

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

s=int(input('Qual é sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[s]))

if computador == 0:
    if s==0:
        print('EMPATE')
    elif s==1:
        print('O jogador VENCEU!')
    elif s==2:
        print('O computador VENCEU!')
    else:
        print('Jogada inválida, tente novamente')
elif computador == 1:
    if s==1:
        print('EMPATE')
    elif s==2:
        print('O jogador VENCEU')
    elif s==0:
        print('O computador VENCEU')
    else:
        print('Jogada inválida, tente novamente')
elif computador == 2:
    if s==2:
        print('EMPATE')
    elif s==0:
        print('O jogador VENCEU')
    elif s==2:
        print('O computador VENCEU')
    else:
        print('Jogada inválida, tente novamente')