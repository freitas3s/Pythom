# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product
from pesquisaBinaria import pesquisa

def print_iter(iterator):
    print(*list(iterator), sep='\n')



pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca','verde','azul'],
    ['pp','p', 'm', 'g','gg'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]
print_iter(product(*camisetas))
lista_camisetas= [
    camiseta for camiseta in product(*camisetas)
                  ]

print(pesquisa(lista_camisetas,('preta','p','masculino','algodão')))