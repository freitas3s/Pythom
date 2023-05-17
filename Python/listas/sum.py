num=[0,3,4,6]
resultado=9
def soma(num, resultado):
    for j,i in enumerate(num):
        diferenca= resultado - i
        if diferenca in(num):
            print(j)

soma(num,resultado)