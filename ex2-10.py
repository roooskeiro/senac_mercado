num=int(input('Informe um numero: '))
resto=num%5
match resto:
    case 0:
        print('É divisivel por 5')
