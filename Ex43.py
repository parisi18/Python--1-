print('Para calcular o IMC, insira os dados:')
#pedir os dados
s=float(input('Qual é seu peso: '))
s2=float(input('Qual é a sua altura: '))

#calculo IMC
IMC=s/pow(s2,2)

if IMC<18.5:
    print('Abaixo do peso')
    print('Seu IMC é {:.2f}'.format(IMC))

elif IMC>=18.5 and IMC<25:
    print('Peso ideal')
    print('Seu IMC é {:.2f}'.format(IMC))

elif IMC>=25 and IMC<30:
    print('Sobrepeso')
    print('Seu IMC é {:.2f}'.format(IMC))

elif IMC>=30 and IMC<40:
    print('Obesidade')
    print('Seu IMC é {:.2f}'.format(IMC))

else:
    print('Obesidade mórbida')
    print(IMC)