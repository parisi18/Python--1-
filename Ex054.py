from datetime import date #importar biblioteca
anohoje=date.today().year #ano atual
print(anohoje)
i=0 #variável vazia
maior=0 #variável vazia
menor=0 #variável vazia
for c in range (0,7): #na sequencia de 6 itens
    ano = int(input(('Qual o ano de nascimento da {}ª pessoa?: '.format(c))))
    idade=anohoje-ano #calculo da idade
    if idade<21: #se for menor que 21
        menor+=1 #somo na qtd de pessoas
    else: #se for maior que 21
        maior+=1 #somo na qtd de pessoas

print('Existem {} maiores de idade'.format(maior))
print('Existem {} menores de idade'.format(menor))