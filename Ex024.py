import time
n=str(input('Digite a cidade em que você mora: ')).strip()
#printar o inicio da frase passando para MAIUSCULAS e vendo se é igual a 'SANTO'
print('\033[1;34mVerificando\033[m se a cidade começa com Santo...')
time.sleep(2)
print(n[:5].upper() =='SANTO')


