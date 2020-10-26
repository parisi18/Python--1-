s=float(input('Qual o primeiro valor: '))
s2=float(input('Qual o segundo valor: '))
s3=float(input('Qual o terceiro valor: '))

m=s #a menor variável definida por escolha minha
#se s3<s2
if s2<s and s3<s2:
    m=s3 #o menor passa a ser s3
    print('O menor valor digitado foi \033[4m{}\033[m'.format(m))
    print('O maior valor digitado foi \033[4m{}\033[m'.format(s))
#se s3>s2
if s3<s and s2<s3:
    m=s2#o menor passa a ser s2
    print('O menor valor digitado foi \033[4m{}\033[m'.format(m))
    print('O maior valor digitado foi \033[4m{}\033[m'.format(s))
