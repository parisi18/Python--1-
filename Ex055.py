menor=0 #variável vazia
maior=0 #variável vazia
for c in range (1,7): #numa sequencia de 6 itens
    peso=float(input('Qual o peso da {}ª pessoa? '.format(c)))
    if c==1: #se for a primeira pessoa
        maior=peso #atribuo a variável
        menor=peso #atribuo a variável
    else:
        if peso>maior: #se o peso for maior q a atribuida inicialmente
            maior=peso #toma lugar da variável
        elif peso < maior: #se o peso for menor q a atribuida inicialmente
            menor=peso #toma lugar da variável
print('O maior peso é {} Kg'.format(maior))
print('O menor peso é {} Kg'.format(menor))
