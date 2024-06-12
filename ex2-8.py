num=float(input('informe um numero: '))
raiz=num**0.5
quad=num**2
if(num>=0):
    input('a raiz quadrada de {} é {}.'.format(num,raiz))
elif(num<0):
    input('{} elevado ao quadrado é {}.'.format(num,quad))