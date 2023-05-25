lista=[1,3,5,7,9,]
def pesquisa(lista,item):
    baixo=0
    alto=len(lista)-1
    while baixo<=alto:
        meio=(baixo+alto)//2
        chute= lista[meio]
        if chute<item:
            baixo=meio+1
        if chute>item:
            alto=meio-1
        if chute==item:
            return meio
    return None

print(pesquisa(lista,3))