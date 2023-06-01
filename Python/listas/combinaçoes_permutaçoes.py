# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product
from pesquisaBinaria import pesquisa
import time

def print_iter(iterator):
    print(*list(iterator), sep='\n')



pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca','verde','azul','amarela','vermelha','rosa','laranja','roxo','cinza',],
    ['pp','p', 'm', 'g','gg','xg','xgg'],
    ['masculino', 'feminino', 'unisex','lgbt'],
    ['social','camiseta','regata','polo','jaqueta'],
    ['algodão', 'poliéster','elastano','drifit',],
    ['calvin','reserva','tommy','lacoste','gucci','armani','renner','riachuelo','cea','zara','polo']
]
#print_iter(product(*camisetas))
lista_camisetas= [
    camiseta for camiseta in product(*camisetas)
                  ]
#print(len(lista_camisetas))
#procurando um item usando um loop for:
print(lista_camisetas.index(('roxo','xgg','unisex','jaqueta','drifit','zara')))
ini1=time.time()
for i in lista_camisetas:
    if i== lista_camisetas.index(('roxo','xgg','unisex','jaqueta','drifit','zara')):
        break
fim1=time.time()

print(fim1-ini1)
#leva quase 2 min e nao achou o indice correto
ini2=time.time()
#usando a pesquisa binaria o tempo cai exponencialmente
print(pesquisa(lista_camisetas,('roxo','xgg','unisex','jaqueta','drifit','zara')))
fim2=time.time()
print(fim2-ini2)
#leva menos de 3 segundos
