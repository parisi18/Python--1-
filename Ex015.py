s=int(input('Quantos dias alugados?: '))
s2=int(input('Quantos Kms percorridos?: '))
p=s*60 #cálculo do preço por dias alugados
p2=s2*0.15 #cálculo do preço por Kms percorridos
print('O preço final será de \033[7;30m{:.2f}\033[mR$'.format(p+p2))