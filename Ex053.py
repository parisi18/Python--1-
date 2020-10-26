frase=str(input('Digite uma frase qualquer: ')).strip().upper()
palavras=frase.split() #separo em lista
junto=''.join(palavras) #junto sem espaços
inverso='' #variável vazia
'''inverso = frase[::-1]''' #LEIO A PALAVRA DO INICIO AO FIM DE TRAS P FRENTE
'''print(palavra,inverso)'''
'''if palavra == inverso: # SE FOREM IGUAIS, SÃO PALINDROMOS
    print('Essa palavra é um PALÍNDROMO')
else:
    print('Essa palavra NÃO é um PALÍNDROMO')'''
for letras in range (len(junto)-1,-1,-1): #leio a palavra completa, iniciando do final, indo de trás pra frente
    inverso += junto[letras] #inverso é a junção das letras da sequência
print(inverso)