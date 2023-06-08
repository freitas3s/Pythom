
def pesquisa(lista,item):
    baixo=0
    alto=len(lista)-1
    contagem=0
    while baixo<=alto:
        print(f'tempo {contagem}')
        meio=(baixo+alto)//2
        chute= meio
        if chute<lista.index(item):
            baixo=meio+1
        if chute>lista.index(item):
            alto=meio-1
        if chute==lista.index(item):
            return meio
        contagem+=1
    return None

#lista=[numero for numero in range(1000000000)]





#print(pesquisa(lista,960468400))