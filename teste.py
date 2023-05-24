def soma(a,b):
    lista1=[]
    lista2=[]
    resultado=[]
    for i in str(a) :
        lista1.append(i)
    lista1.reverse()

    while len(lista2)<len(lista1):
        lista2.append(str(0))

    for i in str(b):
        lista2.append(i)
    lista2.reverse()


    resto=0
    for i in range(len(lista1)):
        soma=int(lista1[i])+int(lista2[i])+resto


        if soma>=10:
            diferença=soma-10
            resto=1
            resultado.append(diferença)
        else:
            resto=0
            resultado.append(soma)


    resultado.reverse
    return resultado

    
print(soma(9999999,9999))