from random import choice
#importar a biblioteca ramdom

#colocar os nomes que vão para sorteio
a=str(input('Digite o nome do 1º aluno: '))
a2=str(input('Digite o nome do 2º aluno: '))
a3=str(input('Digite o nome do 3 aluno: '))
a4=str(input('Digite o nome do 4º aluno: '))
lista = [a,a2,a3,a4]
#sortear os nomes
s= choice(lista)
print('O aluno escolhido foi \033[1;30;41m{}\033[m'.format(s)) #mostrar o nome sorteado