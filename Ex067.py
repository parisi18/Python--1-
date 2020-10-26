mult=0 #variavel nula
while True:
    num = int(input('Quer ver a tabuada de qual número?: '))
    if num<0:
        break
    for c in range(1,11): #numa sequencia de 10 numeros
        mult=num*c #mostro a multiplic
        print(f'{num} x {c} = {mult}')
    print('-=' * 10)
print('Tabuada finalizada, volte sempre')
