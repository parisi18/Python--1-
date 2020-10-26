s=int(input('Digite uma medida em metros: '))
c=s*100 #equivalente em centímetros
c1=s*1000 #equivalente em milímetros
print('A medida possui \033[1;31m{}\033[m centímetros e \033[1;32m{}\033[m milímetros'.format(c,c1))
