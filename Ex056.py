idtot=0 #variável vazia
velho=0 #variável vazia
totmulher=0 #variável vazia
nomevelho='' #variável vazia
for c in range (1,5): #numa sequencia de 4 itens
    print('-----{}ª PESSOA-----'.format(c))
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).upper().strip()
    idtot += idade #somo a idade total
    if c==1 and sexo in 'Mm': #primeiro masculino
        velho=idade
        nomevelho=nome
    if sexo in 'Mm' and idade>velho: #prox masculino mais velho que o primeiro
        velho=idade
        nomevelho=nome
    if sexo in 'Ff' and idade <20: #feminina idade menor que 20 anos
        totmulher += 1

print('A média da idade do grupo é {} anos'.format(idtot/4))
print('O homem mais velho tem {} anos e se chama {}'.format(velho,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))
