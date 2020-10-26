s=str(input('Digite uma frase qualquer: ')).strip()
#passa tudo para MAIUSCULO
s2=s.upper()
#mostrar quantas vezes aparece o 'A'
print('A letra A aparece \033[1;31m{}\033[m vezes'.format(s2.count('A')))
#em que posição a letra 'A' aparece pela primeira vez
print('A letra A aparece na posição \033[1;30m{}\033[m pela 1ª vez'.format(s2.find('A')+1))
#Em que posição a letra 'A' aparece pela última vez
print('A última letra A apareceu na posição: \033[1;37m{}\033[m'.format(s.rfind('A')+1))