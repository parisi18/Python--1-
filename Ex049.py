s=int(input('Digite um número entre 0 e 10:'))#pedir o núm
print('A tabuada completa do número {}'.format(s))
print('='*10)
for c in range(1,11):#na seq de 1 a 10
    print('{} x {} = {}'.format(c,s,c*s)) #printar a tabuada