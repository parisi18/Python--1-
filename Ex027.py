s=str(input('Digite seu nome completo: '))
print('\033[4;34mMuito\033[m prazer em te conhecer!')
#dividir em listas
s2=s.split()
#primeira lista
print('Seu primeiro nome é \033[;;41m{}\033[m'.format(s2[0]))
#printar o ultimo elemento da lista na ultima posição
print('Seu último nome é \033[;;41m{}\033[m'.format(s2[-1]))
