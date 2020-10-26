from random import shuffle
#importar as escolhas aleatórias

n=str(input('Digite o nome do 1º aluno: '))
n2=str(input('Digite o nome do 2º aluno: '))
n3=str(input('Digite o nome do 3º aluno: '))
n4=str(input('Digite o nome do 4º aluno: '))

lista=[n,n2,n3,n4]

# embaralha a lista anterior
shuffle(lista)

#printa a lista anterior
print('A ordem de apresentação será: \n\033[1;31m{}\033[m'.format(lista))



