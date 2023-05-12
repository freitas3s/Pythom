print("Dê o seu depoimento e contribua para a investigação")
print("")

telefonou = input("Ligou para vitima?")
if telefonou == "sim":
    telefonou = int(1)
else: 
    telefonou = int(0)
local = input("Esteve no local do crime?")
if local == "sim":
    local = int(1)
else:
    local = int(0)
onde_mora = input("Mora proximo a vitima?")
if onde_mora == "sim":
    onde_mora= int(1)
else:
    onde_mora = int(0)
 
devia = input("Devia para a vitima?")
if devia == "sim":
    devia= int(1)
else:
    devia = int(0)

trabalhou = input("Já trabalhou com a vítima?")
if trabalhou == "sim":
    trabalhou= int(1)
else:
    trabalhou = int(0)

depoimento = telefonou + local + onde_mora + devia + trabalhou
if depoimento < 2 :
    print("Está liberado!")
if depoimento == 2 :
    print ("Você é suspeito!!!")
if depoimento == 3 or depoimento == 4 :
    print("Você é provavelmente um cúmplice!!!")

if depoimento == 5 :
    print("Você é o assasino e está preso!!!")