prod=('Lápis', 1.75 #crio a tupla
      ,'Borracha', 2
      ,'Caderno', 15.90
      ,'Estojo', 25
      ,'Transferidor', 4.20
      ,'Compasso', 9.99
      ,'Mochila', 120.32
      ,'Canetas', 22.30
      ,'Livro', 34.90)
print('-='*20)
print(f'{"LISTAGEM DE PREÇOS":^40}') #centralizado com 40 espaços
print('-='*20)
for pos in range (0,len(prod)): #crio a posição de acordo com o tamanho da lista
    if pos%2==0: #se a posição for par é produto
        print(f'{prod[pos]:.<30}',end='')
    else: #se for impar é preço
        print(f'R${prod[pos]:>7.2f}')