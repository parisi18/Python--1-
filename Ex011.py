s=int(input('Digite a largura da parede(em metros): '))
s2=int(input('Digite a altura da parede(em metros): '))
print('Calculando a quantidade de tinta necessária...')
c1=s*s2 #área da parede
c2=c1/2 # a quantidade de litros de tinta necessária pra pintar a parede
print('Serão necessários \033[0;36m{}\033[m litros de tinta'.format(c2))
