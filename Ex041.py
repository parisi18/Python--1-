from datetime import date

print('Para saber sua categoria, insira o ano de nascimento')
atual= date.today().year #ano atual

s=int(input('Seu ano de nascimento (XXXX): '))

idade= atual-s #calcular a diferença de anos

if idade <=9: #se idade menor que 9
    print('Sua categoria é MIRIM')
elif 9<idade<=14: #idade entre 9 e 14
    print('Sua categoria é INFANTIL')
elif 14<idade<=19: #idade entre 14 e 19
    print('Sua categoria é JÚNIOR')
elif 19<idade<=25: #idade entre 19 e 25
    print('Sua categoria é SÊNIOR')
else: #idade maior que 25
    print('Sua categoria é MASTER')



