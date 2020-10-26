print('Gerador de PA')
print('-='*10)
n1=int(input('Primeiro termo: '))
r=int(input('Razão: '))
c=1 #contador inicia no primeiro termo
termo=n1#criar uma variável para o input do primeiro termo
while c<=10: #até o decimo termo
    print('{} -> '.format(termo),end='') #printar com seta
    c+=1 #somar o contador com 1
    termo+=r #ir somando a razao
print('FIM')