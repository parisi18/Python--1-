import emoji
from time import sleep
print('====='*5,'CONTAGEM REGRESSIVA','====='*5)
for c in range(10,-1,-1):#dentro da sequencia de 1 a 10 conte ao contrário
    sleep(1)#a cada 1 seg
    print(c)#conte um numero
    if c==0:#quando for o final
        print(':wink:')