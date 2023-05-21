import math


def equacao(a,b,c):
    if a == 0:
        print("não é do 2 grau: ")
    delta= b^2 -(4*a*c)
    if delta <0:
        print("nao possui raizaes reais ")
    
    x1= (-b+ math.sqrt(delta))/2*a
    x2= (-b- math.sqrt(delta))/2*a
    print("x1= ",x1)
    print("x2= ",x2)

equacao(1,0,-9)