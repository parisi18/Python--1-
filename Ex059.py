n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))
opc=0
while opc !=5: #enquanto a opção não for 5
    print('''Selecione uma opção:
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA''')
    opc = int(input('Qual é a sua opção?'))
    print('-='*10)
    if opc==1: #opção soma
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1,n2,soma))
    elif opc==2: #opção mult
        mult=n1*n2
        print('A multiplicação entre {} e {} é {}'.format(n1,n2,mult))
    elif opc==3: #opção maior
        if n1>n2:
            print('O maior entre {} e {} é {}'.format(n1,n2,n1))
        else:
            print('O maior entre {} e {} é {}'.format(n1,n2,n2))
    elif opc==4: #opção novo valor
        n1 = int(input('Primeiro novo valor: '))
        n2 = int(input('Segundo novo valor: '))
    elif opc==5: #finalizar
        print('FINALIZANDO...')
    else:
        print('Opção inválida')
print('FIM')