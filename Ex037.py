print('''Selecione o modo de conversão:
Insira [1] converter para binário
Insira [2] converter para octal
Insira [3] converter para hexadecimal''')

s2=int(input('Dentre as alternativas de conversão, qual deseja usar?: '))
s=int(input('Digite o número que deseja converter: '))

if s2 == 1:
    print('O número {} em binário será {}'.format(s,bin(s)))
elif s2 == 2:
    print('O número {} em octal será {}'.format(s,oct(s)))
elif s2 == 3:
    print('O número {} em hexadecimal será {}'.format(s,hex(s)))
else:
    print('Opção inválida, tente novamente')

