clubes='Atlético-MG','Internacional','Flamengo','São Paulo','Fluminense','Santos','Palmeiras','Fortaleza','Atlético-GO','Sport Recife','Grêmio','Vasco da Gama','Ceará','Corinthians','Botafogo','Coritiba','Bahia','Atlético-PR','Bragantino-SP','Goiás'
print(f'Os 5 primeiros são {clubes[0:5]} ')
print(f'Os 4 últimos são {clubes[-4:]}')
print(f'Os times em ordem alfabética são {sorted(clubes)}')
s=clubes.index('Corinthians')
print(f'Corinthians esta na posição {s+1}')


