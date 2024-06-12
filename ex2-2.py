num1=int(input('informe um numero: '))
num2=int(input('informe outro numero: '))
if(num1>num2):
    print('{} é maior que {}'.format(num1,num2))
elif(num2>num1):
    print('{} é maior que {}'.format(num2,num1))
else:
    print('{} é igual a {}'.format(num1,num2))