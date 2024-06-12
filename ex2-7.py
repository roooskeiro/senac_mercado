num1=int(input('informe um numero: '))
num2=int(input('informe outro numero: '))
soma=num1+num2
soma8=soma+8
soma5=soma-5
if(soma<20):
    input('a soma de {} mais {} da é igual a {}, que mais 8 da {}'.format(num1,num2,soma,soma8))
elif(soma>20):
    input('a soma de {} mais {} da é igual a {}, que menos 5 da {}'.format(num1,num2,soma,soma5))
