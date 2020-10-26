s=str(input('Qual é seu nome completo?: '))
#procurar SILVA no nome digitado todo passado para MAIUSCULAS
print('Seu nome tem Silva?: \033[1;32m{}\033[m'.format('SILVA' in s.upper()))
