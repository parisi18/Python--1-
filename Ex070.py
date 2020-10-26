total=totmil=menor=cont=0
barato=' '
while True:
    prod=str(input('Qual o nome do produto? ')).strip()
    preco=float(input('R$'))
    cont+=1
    total+=preco
    if preco>1000:
        totmil+=1
    if cont==1 or preco<menor:
        menor=preco
        barato=prod
    opc=' '
    while opc not in 'SN':
        opc = str(input('Quer continuar?[S/N]')).upper().strip()
    if opc=='N':
        break
print(f'O total da compra foi {total}')
print(f'Temos {totmil} produtos custando mais R$1000')
print(f'O produto mais barato foi {barato} que custou {menor:.2f}')

