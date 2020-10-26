primeiro=int(input('primeiro termo: '))#primeiro termo
razao=int(input('Razão: ')) #razão da PA
decimo = primeiro + (10-1)*razao #decimo termo
for c in range(primeiro,decimo+razao,razao):
    print('{}'.format(c),end ='->')
print('Acabou')