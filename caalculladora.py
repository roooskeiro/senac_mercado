def calculadora():
    while True:
        ope = input('selecione uma função +, -, *, /, **, ^: '):
        if ope == '+'

















if ope == '+':
    def soma(num1, num2):
        return num1 + num2
    num1 = int(input('informe o 1 numero: '))
    num2 = int(input('informe o 2 numero: '))
    res = soma(num1, num2)
    print(f'{num1} + {num2} = {res}')

elif ope == '-':
    def subt(num1, num2):
        return num1 - num2
    num1 = int(input('informe o 1 numero: '))
    num2 = int(input('informe o 2 numero: '))
    res = subt(num1, num2)
    print(f'{num1} - {num2} = {res}')


elif ope == '*':
    def mult(num1, num2):
        return num1 * num2
    num1 = int(input('informe o 1 numero: '))
    num2 = int(input('informe o 2 numero: '))
    res = mult(num1, num2)
    print(f'{num1} * {num2} = {res}')

elif ope == '/':
    def divi(num1, num2):
        return num1 / num2
    num1 = int(input('informe o 1 numero: '))
    num2 = int(input('informe o 2 numero: '))
    res = divi(num1, num2)
    print(f'{num1} / {num2} = {res}')

elif ope == '**':
    def expo(num1, num2):
        return num1 ** num2
    num1 = int(input('informe o 1 numero: '))
    num2 = int(input('informe o 2 numero: '))
    res = expo(num1, num2)
    print(f'{num1} elevado a {num2} = {res}')






else:
    print(f'função invalida')

calculadora()
