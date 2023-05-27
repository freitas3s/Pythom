# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
l1= ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2= ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


def zipper(lista1,lista2):
    intervalo=min(len(lista1),len(lista2))
    return [
        (lista1[i],lista2[i]) for i in range(intervalo)
    ]

print(zipper(l1,l2))
