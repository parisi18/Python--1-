#manipulando texto
frase='Curso em Vídeo Python'
len(frase)
frase.count('o') #contar quantas vezes aparece a letra o minúscula
frase.count('o',0,13) # conta do 1º ao 12º caractere
frase.find('deo')# quantas vezes aparece 'deo', mostra onde começa
#existe também o frase.rfind e frase.lfind
frase.find('Android') # vai mostrar -1 pois essas palavra não tem na frase
'Curso' in frase # mostra true or false se curso está em frase

#TRANSFORMAÇÃO
frase.replace('Python', 'Android') #troca Python por Android
frase.upper() #deixa tudo maiúsculo
frase.lower() #deixa tudo minúsculo
frase.capitalize() #deixa só o primeiro caractere em maiusculo
frase.title() #deixa o primeiro caractere de cada palavra da string maiusculo
frase.strip() #tira os espaços antes e depois da string
frase.lstrip() #tira os espaços do lado esquerdo
frase.rstrip() #tira os espaços do lado direito

#DIVISÃO
frase.split() #cria uma lista com as palavras da frase

#JUNÇÃO
'-'.join(frase) #coloca - nos espaços vazios da frase