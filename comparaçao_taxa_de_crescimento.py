
exercicio= True
while exercicio == True:
    pais_1= input("DIgite a taxa da populacao do pais 1: ")
    pais_2= input("DIgite a taxa da populacao do pais 2: ")
    taxa_1= (input("Digite a taxa de crescimento ao ano do pais 1 : "))
    taxa_2=(input("Digite a taxa de crescimento ao ano do pais 2 : "))
    ano=0
    valores_validos=None
    try:
        pais_1=float(pais_1)
        pais_2=float(pais_2)
        taxa_1=float(taxa_1)
        taxa_2=float(taxa_2)
        valores_validos= True
    except:
        valores_validos= None
    if valores_validos is None:
        print("digite apenas numeros!!!")
        continue

    while pais_1 < pais_2:
        pais_1 = pais_1 + pais_1*(taxa_1/100)
        pais_2 = pais_2 + pais_2*(taxa_2/100)
        ano += 1
    print (f"anos necessarios: {ano}")
    resposta=True
    while resposta == True:
        resposta=input("deseja repetir a pesquisa? digite 'sim' ou 'nao' : ")
        if resposta == "sim":
            exercicio=True
            resposta = False
        elif resposta== "nao":
            exercicio= False
            resposta = False
        else:
            print("resposta invalida!")
            resposta=True
   
    
    if resposta == "sim":
        exercicio= True

print("ate mais")