resp='Ss' #a unica resp para continuar
quant = soma = maior = menor = 0 #variáveis iniciam nulas
while resp in 'Ss': #enquanto quiser continuar
    num=int(input('Digite um número: '))
    soma += num #soma os numeros
    quant +=1 #conta mais um
    if quant==1: #se for o primeiro
        maior=menor=num #esse numero se tornar o menor e maior
    else: #depois do primeiro
        if num>maior:
            maior=num #se for o maior
        if num<menor:
            menor=num #se for o menor
    resp=str(input('Você quer continuar [S/N]?')).strip().upper()#retira espaço e coloca em maiusculo
med=soma/quant
print('Você digitou {} números e a média foi {:.2f}'.format(quant,med))
print('O maior número foi {} e o menor foi {}'.format(maior,menor))