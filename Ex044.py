#informar as condições
print('Condições de pagamento:')
print('SELECIONE (1)- À vista no DINHEIRO/CHEQUE : 10% off')
print('SELECIONE (2)- À vista no CARTAO: 5% off')
print('SELECIONE (3)- Em até 2x no cartão: sem juros')
print('SELECIONE (4)- 3x ou mais no cartão: 20% de juros')

#pedir a condição de o preço
s1=float(input('Qual o preço do produto? '))
s=int(input('Selecione o método(1-4) de pagamento? '))

#métodos

if s==1:
    s1 = 0.9 * s1  # 10%off
    print('O preço do será:{}R$'.format(s1))

elif s==2:
    s1 = 0.95 * s1  # 5% off
    print('O preço será: {}R$'.format(s1))

elif s==3:
    s1 = s1 / 2  # 2 parcelas
    print('O preço da parcela será {:.2f}'.format(s1))

elif s==4:
    n=int(input('Quantas parcelas?'))
    p = (s1 / n)+(0.2*(s1/n))  # n parcelas + 20%
    final= n*p
    print('O preço da parcela será {}R$\n Sua compra será de {}R$'.format(p,final))
