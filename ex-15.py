i = 1
while True:
#while i<6:
#for i in range(1,6):
    print(i)
    nome=input(f'informe o nome {i}: ')
    idade=int(input(f'informe a idade {i}: '))
    if(idade>=18):
        print(f'{nome} é maior de idade')
    else:
        print(f'{nome} é menor de idade')
    i+=1

