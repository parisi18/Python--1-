from random import randint
from time import sleep
print('-=-'*15)
print('Vou \033[4;31mpensar\033[m em um número de 0 a 5. Tente adivinhar...')
print('-=-'*15)
num=int(input('Em que número eu pensei? => '))
s=randint(0,5) #aleatório entre 0-5
print('O número que eu escolhi foi...')
sleep(2) #tempo de espera
print(s)
if num == s: #se for igual printa Parabéns
    print('\033[4;32mParabéns\033[m, você é FODA!')
else:#se não printa hahaha
    print('Hahaha, \033[0;31meu venci\033[m')

