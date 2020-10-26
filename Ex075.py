n=(int(input('Digite um número: ')),
   int(input('Digite outro número: ')),
   int(input('Digite mais um número: ')),
   int(input('Digite o último número: ')))
if n.count(9)>1:
    print(f'O nove apareceu {n.count(9)} vezes') #conta os 9
else:
    print(f'O nove apareceu {n.count(9)} vez') #se for mais de 1 vez
print(f'O primeiro três foi digitado na {n.index(3)+1}ª posição') #mostra a posição
for c in n:
    if c%2==0: #se for par
        print(f'par = {c}',end=' ')

