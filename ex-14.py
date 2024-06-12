texto=""
while texto != "sair":
    print(" ")
    texto=str(input('Insira uma palavra para ser invertida: '))
    tamanho_texto=len(texto)-1

    if texto == 'SAIR' or texto == 'sair':
        print('Você saiu')
    else:
        while tamanho_texto >=0:
            print(texto[tamanho_texto],end='')
            tamanho_texto -=1
