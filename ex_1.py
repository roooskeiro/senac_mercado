'''
Crie um programa que leia um nome completo de uma pessoa e mostre 
- O nome com todas as letras maiúsculas e minúsculas;  
- Quantos letras ao todo (sem contar espaços); 
- Quantas letras tem o primeiro nome.
'''


# pnom = str(input('Informe seu primeito nome: '))
# snom = str(input('Informe seu segundo nome: '))
# tnom = str(input('Informe seu terceiro nome: '))
# nome = (f'{pnom} {snom} {tnom}')
# print(nome)




cont = 0

nome = str(input('Informe seu nome: '))
print(nome)

maiu = nome.upper()
print(maiu)
minu = nome.lower()
print(minu)

sees = nome.replace(' ', '')
qule = len(sees)
print(qule)

while True:
    if nome[cont] == ' ':
         break
    cont = cont+1
    if cont == len(nome):
        break
print(cont) 