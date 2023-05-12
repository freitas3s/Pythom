lista_compras= []
print("selecione uma opçao")

while True:
    opçoes=input('[i]nserir [a]pagar [l]istar: ')
    if opçoes== 'i':
        itens_adicionados= input("digite o item que deseja adicionar a lista: ")
        lista_compras.append(itens_adicionados)
        print(itens_adicionados,' adicionado a lista')
        continue
    elif opçoes== "a":
        itens_removidos=input("digite o item que deseja remover da lista: ")
        if len(lista_compras)==0:
            print('nao ha nada para remover')
            continue
        if itens_removidos not in lista_compras:
            print("este item não esta na lista!")
            continue
        lista_compras.remove(itens_removidos)
    elif opçoes== 'l':
        for indice, produto in enumerate(lista_compras):
            print(indice, produto)
            continue
    else:
        print('digite apenas i a ou l!!!')
        continue
    