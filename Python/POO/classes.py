#classe = molde sem dados 
#instancia da classe tem dados 
#umas classe pode gerar varias instancias
#na classe o self é a propria instancia
import json
import os 
path=r'C:\Users\guije\Documents\GitHub\teste\Python\POO\pessoas.json'
class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade=idade

def cria_pessoa(nome,idade):
    dados.append(pessoa(nome,idade))


#salvando em JSON:
dados = []

while len(dados) <4:
    nome=input('nome ')
    idade=int(input('Idade '))
    os.system("cls")
    cria_pessoa(nome,idade)

dados_formatados = [
    vars(item) for item in dados
]

with open(path, 'w') as arquivo:
    json.dump(dados_formatados,arquivo,ensure_ascii=False,indent=2)