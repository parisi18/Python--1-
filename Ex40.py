print('Para calcular a média da nota, insira os dados: ')
s=float(input('Digite a primeira nota: '))
s2=float(input('Digite a segunda nota: '))

#calculo da média
med=(s+s2)/2

if med<5: #média menor que 5
    print('Sua média foi {}, você foi REPROVADO'.format(med))
elif 5<=med<=6.9: #média entre 5 e 6,9
    print('Sua média foi {}, você está de RECUPERAÇÃO'.format(med))
else: #média acima de 6.9
    print('Sua média foi {}, você está APROVADO'.format(med))

