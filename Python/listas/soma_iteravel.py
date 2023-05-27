def soma(a,b):
    lista1=[]
    lista2=[]
    resultado=[]
    def criar_lista(x,lista):
        for i in str(x):
            lista.append(i)
        lista.reverse() 

    criar_lista(a,lista1)

    while len(lista2)<len(lista1):
        lista2.append(str(0))

    criar_lista(b,lista2)
    
    resto=0
    for i in range(len(lista1)):
        soma=int(lista1[i])+int(lista2[i])+int(resto)

        if soma>=10:
            diferença=soma-10
            resto=1
            resultado.append(diferença)
        else:
            resto=0
            resultado.append(soma)


    resultado.reverse()
    return resultado


print(soma(150,255))
