lista_de_compras = []
opcao = 1

while opcao != 0:
#while True:
    
    print('1 inserir')
    print('2 excluir')
    print('3 listar')
    print('0 sair')

    opcao = input('qual opcao? ')

    if opcao == '1':
        print('inserir')
        item = input('qual item? ')
        lista_de_compras.append(item)
        print(lista_de_compras)
    
    elif opcao == '2':
        
        item_para_excluir = input('qual item deseja excluir? ')
        tamanho_da_lista = len(lista_de_compras)
        
        for posicao in range(tamanho_da_lista):
            print(posicao, lista_de_compras[posicao])
            if lista_de_compras[posicao] == item_para_excluir:
                print(f'{item_para_excluir} foi apagado')
                lista_de_compras.pop(posicao)
       
                break
    




    
    elif opcao == '3':
        print('listar')

        tamanho_da_lista = len(lista_de_compras)
        for posicao in range(tamanho_da_lista):







    elif opcao == '4':
        print('editar')











    
    # elif opcao == '0':
    #     print('saindo...')
    #     break

    else:
        print('opcao invalida...')