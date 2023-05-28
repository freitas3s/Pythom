print("Dê o seu depoimento e contribua para a investigação")
print("")

telefonou = input("Ligou para vitima?")

def somador(resposta):
    
    if resposta== "sim":
        return 1
    else: 
        return 0

contador=somador(telefonou)

local = input("Esteve no local do crime?")
contador+=somador(local)
onde_mora = input("Mora proximo a vitima?")
contador+=somador(onde_mora)
devia = input("Devia para a vitima?")
contador+=somador(devia)

trabalhou = input("Já trabalhou com a vítima?")
contador+=somador(trabalhou)

depoimento = contador

if depoimento < 2 :
    print("Está liberado!")

if depoimento == 2 :
    print ("Você é suspeito!!!")

if depoimento == 3 or depoimento == 4 :
    print("Você é provavelmente um cúmplice!!!")

if depoimento == 5 :
    print("Você é o assasino e está preso!!!")