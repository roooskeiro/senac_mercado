opcao=1
while opcao != 5:
    print('menu')
    print('1.cadastro')
    opcao = int(input('opção desejada: '))




nome=input('Informe um nome: ')
tipo=input('qual é o tipo do produto: ')
preço=float(input('quanto custa o produto: '))
peso=float(input('qual é o peso do produto: '))



dicio={
    'nome': nome,
    'tipo': tipo,
    'preço': preço,
    'peso': peso
}

print(dicio)