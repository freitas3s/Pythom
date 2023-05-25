carros=[
{"Nome": "fusca",
"Km por litro": 7},

{"Nome": "gol",
"Km por litro": 10},

{"Nome": "uno",
"Km por litro": 12.5},

{"Nome": "Vectra",
"Km por litro": 9},

{"Nome": "Peugeout",
"Km por litro": 14.5}]
menorvalor=[100000]
carro_de_menor_valor=[0]
for carro in carros:
    consumo=1000/carro["Km por litro"]
    carro.setdefault("consumo", consumo)
    Valor_gasolina=consumo*2.25
    carro.setdefault("Valor",Valor_gasolina)
    print(carro)

    
for carro in carros:
    if carro["Valor"] < menorvalor[0]:
        menorvalor.pop()
        menorvalor.append(carro["Valor"])
        carro_de_menor_valor.pop()
        carro_de_menor_valor.append(carro["Nome"])

    else:
        None

print(f"melhor consumo: ", carro_de_menor_valor)
