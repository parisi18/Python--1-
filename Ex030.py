s=float(input('Me diga um número qualquer: '))
if s%2 == 0:#se for divisível por 2
    print('O número {} é \033[4;35mPAR\033[m!'.format(s))
else:
    print('O número {} é \033[4;32mÍMPAR\033[m!'.format(s))


