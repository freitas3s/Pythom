lista=["flower","flow","flight"]
comparador= []
def pesquisa(lista):
    #adiciona a primeira letra do primeiro item ao comparador
    contador=0
    comparador.append(lista[0][:contador+1])

    while contador<len(lista):
        for item in lista:
            # se a letra do comparador estiver em todos os itens adicionamos a proxima letra da primeira palavra
            if comparador[0] in item:
                comparador[0]+= item[contador+1:contador+2]
                contador+=1
                continue
            #caso contrario removemos a letra que foi adicionada e terminamos o loop
            else:
                comparador[0]= comparador[0][:-1]
                break

    

pesquisa(lista)
print(comparador)
