'''
Sistema para cadastro de produtos
Voce foi contratado para desenvolver um sistema de cadastro produtos 
para determinada loja,que deve  ser capaz de armazenar informaçoes como
nome, categoria,preço e quantidade em estoque. O sistema deve oferecer
um menu interativo com as seguintes opçoes:

1. cadastro de novo produto
2. editar dados  de um produto
3. excluir um produto
4. listar todos produtos cadastrados
5. sair do sistema
'''


produtos=[]
opsao=1


while opsao != 5:

    print('menu principal')
    print()
    print('1. cadastro de novo produto')
    print('2. editar dados de um prooduto')
    print('3. excluir um produto')
    print('4. listar todos os produtos cadas')
    print('5. sair do sistema')
    print()

    nome=''
    qunt=''
    tipo=''
    preç=''

    opsao = int(input('escolha uma opsao:  '))
    if opsao == 1:
        nome=input('informe o nome do produto: ')
        qunt=int(input('informe a quantidade desse produto: '))
        tipo=input('qual o tipo desse produto:')
        preç=float(input('quanto custa esse produto: '))
        print(f'tem {qunt} {nome}s custa {preç},u {nome} é {tipo}')
        produtos.append(nome) 

    elif opsao ==3:
        produtos.pop(nome)

    elif opsao == 4:
        print(f'tem {qunt} {nome}s custa {preç},u {nome} é {tipo}')

