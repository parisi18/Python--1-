tot18=0
homens=0
mulher20=0
while True:
    idade=int(input('Idade: '))
    sexo= ' '
    while sexo not in 'MF':
        sexo=str(input('Sexo[M/F]: ')).strip().upper()[0]
    if idade>=18: #SE FOR MAIOR DE 18
        tot18+=1
    if sexo=='M': #SE FOR HOMEM
        homens+=1
    if sexo=='F' and idade<20: #SE FOR MULHER E MENOS DE 20
        mulher20+=1
    resp=' '
    while resp not in 'SN': #SE NAO RESP CERTO
        resp=str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
    if resp=='N': #SE N QUISER CONTINUAR
        break
print(f'Total de pessoas com mais de 18 anos {tot18}')
print(f'Total de homens {homens}')
print(f'Total de mulheres com menos de 20 anos {mulher20}')
