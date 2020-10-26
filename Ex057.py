sexo=str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF': #se não for F ou M
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    print('Informação incorreta, preencha novamente')
print('Sexo {} cadastrado com sucesso'.format(sexo))
