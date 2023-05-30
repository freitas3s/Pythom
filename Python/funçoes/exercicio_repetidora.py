"""Faça um programa para imprimir:
            1
            1   2
            1   2    3
            .....
            1   2    3   ...   n
     para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

"""

def repetidora (n):
    texto=str(1)
    for i in range(n):
        print(texto)
        print('')
        texto+= str(i+2)

print(repetidora(10))