palavras=('APRENDER','PROGRAMAR',
          'PYTHON','CURSO','GRÁTIS',
          'ESTUDAR','PRATICAR','TRABALHAR',
          'MERCADO','PROGRAMADOR','FUTURO')
for c in palavras:
    print(f'\nNa palavra {c} temos o ',end='') #analisa cada elemento
    for letra in c: #a cada palavra busco as letras
        if letra.lower() in 'aáãeéêioóôu': #vejo se a letra ta na vogal
            print(letra,end='')
