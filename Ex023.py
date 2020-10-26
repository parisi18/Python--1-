'''n=int(input('Digite um número de 0 a 9999: '))
#dar print colocando os indices desejados mas da erro com menos de 4 digitos
print('unidade: {}'.format(n[3]))
print('dezena: {}'.format(n[2]))
print('centena: {}'.format(n[1]))
print('milhar: {}'.format(n[0]))'''

#ou

n=int(input('Digite um número de 0 a 9999: '))
u=n // 1 % 10
d=n // 10 % 10
c=n // 100 % 10
m=n // 1000 % 10
#fazer os cálculos
print('unidade: \033[1;33m{}\033[m'.format(u))
print('dezena: \033[1;30m{}\033[m'.format(d))
print('centena: \033[1;34m{}\033[m'.format(c))
print('milhar: \033[1;32m{}\033[m'.format(m))