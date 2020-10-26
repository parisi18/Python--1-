numeros='zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treza','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
for num in range(0,21): #na sequencia de 0,20
    num=int(input('Digite um numero entre 0 e 20: '))
    while 0>num or num>20: #se digitar errado
        num = int(input('Digite um numero entre 0 e 20: '))
    print(f'Você digitou o número {numeros[num]}') #PRINTA O NOME DO NUMERO
    break
