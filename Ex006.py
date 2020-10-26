s=int(input('Digite um número: '))
s1=s*2 #o dobro do número
s2=s*3 #o triplo do número
s3=pow(s, (1/2)) # a raíz quadrada
print('O dobro de \033[4;34m{}\033[m é \033[4;34;42m{}\033[m. \nO triplo é \033[4;;41m{}\033[m. \nA raíz quadrada é \033[4;30;45m{:.2f}\033[m.'.format(s, s1, s2,s3))