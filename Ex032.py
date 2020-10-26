from datetime import date
s=int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual: '))

if s==0:
    s=date.today().year #chama a data do sistema
if s%4 == 0 and s%100 != 0 or s%400 == 0:#exceto os múltiplos de 100 que não são múltiplos de 400
    print('Esse ano \033[4;33m{}\033[m \033[0;32mÉ\033[m bissexto'.format(s))
else:
    print('Esse ano \033[0;30;41mNÃO\033[m \033[4;34m{}\033[m é bissexto'.format(s))
