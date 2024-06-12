cont=int(input('informe um numero de repetiçoes: '))
maior=0
for i in range(0,cont,1):
    num=int(input('infome um numero: '))
    if num>maior:
        maior=num
print('o maior numero digitado foi {}.'.format(maior))
