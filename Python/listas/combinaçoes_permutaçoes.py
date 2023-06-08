# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product
from pesquisaBinaria import pesquisa
import time
pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca','verde','azul','amarela','vermelha',
     'rosa','laranja','roxo','cinza',"ciano","anil","azul-bebe",'beje'],

    ['pp','p', 'm', 'g','gg','xg','xgg','exgg'],

    ['masculino', 'feminino', 'unisex','1 ano','5 anos','10 anos','15 anos'],

    ['social','camiseta','regata','polo','jaqueta'],

    ['bermuda', 'calça', 'jeans', 'cargo', 'saia'],

    ['tenis', 'sapatenis', 'sandalia', 'chinelo', 'bota', 'coturno', 'sapato', 'salto'],

    ['algodão', 'poliéster','elastano','drifit','couro'],

    ['calvin','reserva','tommy','lacoste','gucci','armani','renner','riachuelo','cea','zara','polo']
]
#print_iter(product(*camisetas))
lista_camisetas= [
    camiseta for camiseta in product(*camisetas)
                  ]
print(len(lista_camisetas))

print(lista_camisetas.index(('beje','exgg','15 anos','jaqueta','saia', 'salto', 'couro', 'polo')))

print(pesquisa(lista_camisetas,('beje','exgg','15 anos','jaqueta','saia', 'salto', 'couro', 'polo')))



for i in lista_camisetas:
    if i == ('beje','exgg','15 anos','jaqueta','saia', 'salto', 'couro', 'polo'):
        break
    





