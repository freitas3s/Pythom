
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
] 
acertos=0
for pergunta in perguntas:
    print(pergunta["Pergunta"])

    for i,opçao in enumerate(pergunta['Opções']):
        print(f'{i}) {opçao}')


    escolha = int(input("Escolha a resposta"))
    if pergunta["Opções"][escolha] == pergunta["Resposta"]:
        print('você acertou!')
        acertos+=1
    else:
        print("você errou!")
        print("a resposta certa era: ", pergunta["Resposta"])

print(f"você acertou: {acertos}/3 questões")