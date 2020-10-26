print('Sequencia de FIBONACCI')
n=int(input('Quantos termos você quer mostrar?: '))
t1=0 #termo um da fibo
t2=1 #termo dois da fibo
print('{} -> {} '.format(t1,t2),end='')
c=3 #contador inicia no 3
while c<=n: #enquanto o contador for menor que o numero digitado
    t3 = t1 + t2 # a soma dos dois anteriores
    print('-> {} '.format(t3),end='')
    t1=t2 #transportar a variável p frente
    t2=t3 #transportar a variável p frente
    c += 1 #soma mais um no contador
print('-> FIM')