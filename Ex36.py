i=float(input('Qual o valor do imóvel?: '))
i2=float(input('Qual o seu salário?: '))
i3=float(input('Em quantos anos pretende pagar o imóvel?: '))

#calcular o valor da prestação mensal

val=i/(i3*12) #valor da prestação mensal
porc=(30/100)*i2#30% do salário

print('Você terá de pagar {:.2f}R$ por mês durante {:.1f} anos'.format(val,i3))
if val<porc:
    print('Empréstimo \33[4:33mAPROVADO\033[m!')
else:
    print('Empréstimo \033[4:31mNEGADO\033[m!')
