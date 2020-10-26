s=float(input('Primeiro segmento: '))
s2=float(input('Segundo segmento: '))
s3=float(input('Terceiro segmento: '))

if s<s2+s3 and s2<s3+s and s3<s+s2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
