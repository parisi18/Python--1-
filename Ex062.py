print('Gerador de PA')
print('-='*10)
n1=int(input('Primeiro termo: '))
r=int(input('Razão: '))
c=1
termo=n1
total=0 #crio variavel para o numero de termos totais
mais=10 #começa após os primeiros 10 termos do ex 61
while mais!=0:
    total=mais+total #vai somando os 10 + total
    while c<=total: #enquanto c for menor que o total
        print('{} -> '.format(termo),end='')
        c+=1 #soma mais um
        termo+=r #soma a razao
    mais=int(input('Quantos termos a mais você quer mostrar?'))
    print('FIM')
print('Finalizado com {} termos'.format(mais))
