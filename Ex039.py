from datetime import date
anonasc=int(input('Digite seu ano de nascimento: '))

#calcular quantos anos tem:
anoatual=date.today().year
idade=anoatual - anonasc
anof=18-idade
anop=idade-18
if idade<18:
    print('Você ainda irá se alistar no \033[1:31mserviço militar\033[m')
    if anof==1:
        print('Ainda falta \033[1:31m1\033[m ano!')
    else:
        print('Ainda faltam \033[1:31m{}\033[m anos'.format(anof))
elif idade==18:
    print('Está no ano de se alistar no \033[4mserviço militar\033[m')
else:
    if anop==1:
        print('Já se passou \033[1:31m1\033[m ano após o ano de alistamento')
    else:
        print('Já se passaram \033[1:31m{}\033[m anos após o ano de alistamento'.format(anop))

