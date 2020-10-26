s=float(input('Qual a distância da viagem em KM: '))
if s<200: #se a quilometragem for < 200
    p=0.5*s
    print('O preço será \033[4;33m{:.2f}\033[mR$'.format(p))
else:
    p=0.45*s #se a quilometragem for > 200
    print('O preço será \033[4;34m{:.2f}\033[mR$'.format(p))
