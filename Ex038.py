from time import sleep
s=float(input('Digite um número qualquer: '))
s2=float(input('Digite um número qualquer: '))

print('Calculando...')
sleep(2)

if s>s2:
    print('O maior número é \33[4:36m{}\33[m\nO menor número é \33[4:32m{}\33[m'.format(s,s2))
elif s==s2:
    print('Não existe valor maior, os dois são \33[4:30mIGUAIS\33[m!')
else:
    print('O maior número é \033[4:36m{}\033[m\nO menor número é \033[4:32m{}\033[m'.format(s2,s))
