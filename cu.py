def adic (a, b):
    return a + b
def subt (a, b):
    return a - b
def mult (a, b):
    return a * b
def divi (a, b):
    return a / b

def calculadora():
    opera = input('Escolha uma opercão ( +, -, *, /): ')
    num1 = float(input('Informe um numero: '))
    num2 = float(input('Informe outro numero: '))

    if opera == '+':
        resut = adic(num1, num2)
        print(f'{num1} + {num2} = {resut}')
    elif opera == '-':
        resut = subt(num1, num2)
        print(f'{num1} - {num2} = {resut}')
    elif opera == '*':
        resut = mult(num1, num2)
        print(f'{num1} * {num2} = {resut}')
    elif opera == '/':
        resut = divi(num1, num2)
        print(f'{num1} / {num2} = {resut}')
    else:
        print('Operação invalida! ')

calculadora ()

import tkinter as tk

def adnum(num):
    camptext.insert(tk.END, num)

def calcular():
    expre=camptext.get()
    resut=eval(expre)
    camptext.delete(0, tk.END)
    camptext.insert(tk.END, resut)

janel = tk.Tk()

camptext=tk.Entry(janel, width=20)
camptext.grid(row=0, column=0, columnspan=4)

botoes = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3',''
]



    


