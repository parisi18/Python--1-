n=str(input('Digite seu nome completo: ')).strip()
#mostrar o nome em maiúsculas
print('O nome em maiúsculas é: \033[4;33;40m{}\033[m'.format(n.upper()))
#mostrar o nome em minúsculas
print('O nome em minúsculas é: \033[1;31;43m{}\033[m'.format(n.lower()))
#subtrair os espaços do len
print('O número de letras do nome é: \033[1;34;45m{}\033[m letras'.format(len(n)-n.count(' ')))
#o numero de caracteres da lista 0 do split
print('O número de letras no primeiro nome é: \033[1;33;41m{}\033[m letras'.format(len(n.split()[0])))
#ou faço assim buscando o primeiro espaço depois do primeiro nome
print('O número de letras do primeiro nome é: \033[4;35;44m{}\033[m letras'.format(n.find(' ')))