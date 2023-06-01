
def adicionar_item(item):
    to_do.append(item)
    listar(to_do)
    print('')

def listar(to_do):
    if len(to_do) != 0:
        print("TAREFAS:")
        for item in to_do:
            print(item, sep="\n")
    else:
        print('não há itens na lista')

def desfazer(to_do,itens_removidos):
    if len(to_do) != 0:
        item=to_do.pop()
        itens_removidos.append(item)
    listar(to_do)
    return 

def refazer(todo,itens_removidos):
    if len(itens_removidos) == 0:
        print("Não há nada para refazer")
    else:
        todo.append(itens_removidos[-1])
        itens_removidos.pop()
        listar(todo)


to_do= []
itens_removidos=[]
while True:
    comandos=["listar", "desfazer" ,  "refazer"]
    print("Comandos: listar, desfazer e refazer")
    comando=input("digite um comando ou uma tarefa: ") 
    if comando == comandos[0]:
        listar(to_do)
    if comando == comandos[1]:
        desfazer(to_do,itens_removidos)
    if comando == comandos[2]:
        refazer(to_do, itens_removidos)
    if comando not in comandos:
        adicionar_item(comando)