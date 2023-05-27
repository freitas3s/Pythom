def decoradora(func):
    print('decoradora')

    def aninhada(*args,**kwargs):
        print('aninhada')
        resultado=func(*args,**kwargs)
        return resultado+20
    return aninhada

@decoradora
def soma(x, y):
    return x + y

tenPlusfive = soma(10,5)
print(tenPlusfive)