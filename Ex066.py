c=soma=0
while True:
    n = int(input('Digite um número: ')) #COLODO DEPOIS PARA N CONTAR O 999
    if n==999:
        break
    soma += n  # soma os numeros
    c += 1  # conta a quantidade
print(f'Foram digitados {c} números e a soma foi de {soma}')
