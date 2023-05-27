
def pesquisa(lista,item):
    baixo=0
    alto=len(lista)-1
    while baixo<=alto:
        meio=(baixo+alto)//2
        chute= lista.index(lista[meio])
        if chute<lista.index(item):
            baixo=meio+1

        if chute>lista.index(item):
            alto=meio-1

        if chute==lista.index(item):
            return meio
    return None
