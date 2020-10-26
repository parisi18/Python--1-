#padrão ANSI escape sequence
#\33[    => sempre para representar cores e fecha com => m
#\33[style;text;backm
print('\033[0;32m Teste\033[m')
#style - 0 sem estilo   1 em negrito   4 sublinhado   7 inverte as configs
#text - 30 até 37 cores das letras
#30 branco    #33 amarelo    #36 ciano
#31 vermelho  #34 azul       #37 cinza
#32 verde     #35 lilás
#back - 40 até 47 cores de fundo ( a mesma sequencia de cores do text )
#posso criar um dicionário com as cores e depois chamar elas no code
cores={'limpa':'\033[m',
       'azul':'\033[34m',
       'amarelo':'\033[33m',
       'pretoebranco':'\033[7;30m'}
a=3
b=5
print('Os valores são {}{} e {}{}'.format(cores['pretoebranco'],a,cores['amarelo'],b))



