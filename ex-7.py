cont=int(input('informe um numero de repetiçoes: '))
menor=9999
for i in range(0,cont,1):
    num=int(input('infome um numero: '))
    if num<menor:
        menor=num
print('o menor numero digitado foi {}.'.format(menor))