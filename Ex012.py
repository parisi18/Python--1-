s=float(input('Digite o preço do produto: '))
c1=s-((5/100)*s) #Calculo do produto com 5% de desconto
print('Com 5% de desconto: O novo preço será \033[1;35m{:.2f}\033[mR$'.format(c1))
