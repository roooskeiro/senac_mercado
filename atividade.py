'''
Faça uma lista para armazenar dados de pessoas (nome, idade e telefone) usando o formato do dicionario
'''

nome = str(input('informe um nome: '))
idade = int(input('informe a idade do individuo: '))
telefone = (input('informe o numero do individuo: '))

pessoa1 = {
    'nome': nome,
    'idade': idade,
    'telefone': telefone
}

print(pessoa1)