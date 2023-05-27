def parametros_decorador(nome):
    def decorador(func):
        print('decorador:', nome)

        def nova_funcao(*args,**kwargs):
            res=func(*args,**kwargs)
            final=f'{res} {nome}'
            return final
        return nova_funcao
    return decorador

@parametros_decorador(nome='primeiro')
def soma(x,y):
    return x+y

ten_plus_five=soma(10,5)
print(ten_plus_five)

