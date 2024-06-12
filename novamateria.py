# posiçoes 0        1       2      3 
frutas=('banana','manga','maça','pitaya') # tupla de string
print('minha tupla:', frutas)
print('tipo da tupla:',type(frutas))
print('acessando a posiçao 0:', frutas[0])
print('acessando a posiçao 3:', frutas[3])
#frutas[0] = 'pitaya' #o python não suporta alteração de itens pois as tuplas são imutaveis.


#exemplo do exercicio de mes da lista
#1 -  12
#se for menor que um ou maior que 12 - caso de erro
mes = int(input('informe o mes: '))
if (mes < 1 or mes > 12):
    print('mes invalido')
else:
    mesano=('janeiro','fevereiro','março','abril','maio','jjunho','julho','agosto','setembro','outubro','novenbro','desembro')
    