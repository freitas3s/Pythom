
print("Promoçao de carnes!!!")
print(' ')
print ('escolha a sua carne!')
print(' ')
print("1 para file duplo")
print(' ')
print("2 para alcatra")
print(' ')
print("3 para picanha")
print(' ')
again=True


while again== True:
    again=True
    carne_escolhida = input('digite um numero: ')
    numero_valido= None
    try :
        carne_escolhida= int(carne_escolhida)
        numero_valido= True
    except:
        numero_valido= None
    
    if numero_valido == None:
        print("Digite um numero valido!!!")
        continue

    if carne_escolhida == 1 :
        carne_escolhida = 'File duplo'
        print("carne escolhida:", carne_escolhida)
    elif carne_escolhida == 2 :
        carne_escolhida = 'Alcatra'
        print("carne escolhida:", carne_escolhida)
    elif carne_escolhida == 3:
        carne_escolhida = 'Picanha'
        print("carne escolhida:", carne_escolhida)
    else:
        print("digite um numero valido!!!")
        continue
    print(' ')

    quantidade_valida= True
    while quantidade_valida:
        quantidade = input("digite o peso em Kg: " )
        try:
            quantidade= float(quantidade)
            quantidade_valida= False
        except:
            print("digite um numero valido!!!")
            quantidade_valida=True

        
    if quantidade <= 5 and carne_escolhida == 'File duplo' :
        valor_peso = 4.90 * quantidade
        print('valor por kilo= R$ 4,90.') 
        print('Valor total= R$',valor_peso)
    if quantidade >5 and carne_escolhida =='File duplo':
        valor_peso = 5.80 * quantidade
        print('valor por kilo= R$ 5,80.') 
    if quantidade <= 5 and carne_escolhida == 'Alcatra':
            valor_peso = 5.90 * quantidade
            print('valor por kilo= R$ 5,90.') 
    if quantidade > 5 and carne_escolhida == 'Alcatra':
            valor_peso = 6.80*quantidade
            print('valor por kilo= R$ 6,80.')
    if quantidade <= 5 and carne_escolhida == 'Picanha':
        valor_peso = 6.90 * quantidade
        print('valor por kilo= R$ 6,90.') 
    if quantidade > 5 and carne_escolhida == 'Picanha':
        valor_peso = 7.80*quantidade
        print('valor por kilo= R$ 7,80.')

    print('Valor total= R$',valor_peso)

    
    print(' ')

    cartao=True
    while cartao==True:
        print("Pagara com o cartao da loja? ")
        pagamento = input("digite [sim] ou [nao]: ")
        if pagamento =="sim":
            cartao=False
        elif pagamento == "nao":
            cartao= False
        else:
            print("digite apenas sim ou nao!!!")
            cartao= True

    if pagamento == 'sim' and carne_escolhida == 'File duplo':
        valor_desconto = 0.05
        valor_final = valor_peso - valor_peso*valor_desconto
        print("Pagando com o cartão seu desconto será de 5%")
        print("Valor final= R$ ", valor_final)
        print("Obrigado por escolher o Jurubira's Market")
    if pagamento == 'sim' and carne_escolhida == 'Alcatra':
        valor_desconto = 0.05
        valor_final = valor_peso - valor_peso*valor_desconto
        print("Pagando com o cartão seu desconto será de 5%")
        print("Valor final= R$ ", valor_final)
        print("Obrigado por escolher o Jurubira's Market")
    if pagamento == 'sim' and carne_escolhida == 'Picanha':
        valor_desconto = 0.05
        valor_final = valor_peso - valor_peso*valor_desconto
        print("Pagando com o cartão seu desconto será de 5%")
        print("Valor final= R$ ", valor_final)
        print("Obrigado por escolher o Jurubira's Market")
    if pagamento == 'nao' and carne_escolhida == 'File duplo':
        valor_final=valor_peso
        print("Nenhum desconto no valor final")
        print("Valor final = R$ ", valor_peso)
        print("Obrigado por escolher o Jurubira's Market")
    if pagamento == 'nao' and carne_escolhida == 'Alcatra':
        valor_final=valor_peso
        print("Nenhum desconto no valor final")
        print("Valor final = R$ ", valor_peso)
        print("Obrigado por escolher o Jurubira's Market")
    if pagamento == 'nao' and carne_escolhida == 'Picanha':
        valor_final=valor_peso
        print("Nenhum desconto no valor final")
        print("Valor final = R$ ", valor_peso)
        print("Obrigado por escolher o Jurubira's Market")

    print(" ")


    print('Cupom fiscal')
    print(' ')
    print("Carne escolida =", carne_escolhida)
    print ("Peso:", quantidade, "Kg")
    print("Valor total= R$ ", valor_peso)

    if pagamento == 'sim':
        print("pagamento no cartao")
        print("Desconto de: 5%")
    elif pagamento== "nao":
        print("Sem desconto para essa compra")

    print("Valor total= R$", valor_final)
    print("Obrigado por escolher o Jurubira's Market")
    resposta= True
    while resposta == True:
        resposta=input('pressione <s> para continuar e <n> para encerrar' ).lower()
        if resposta == "s":
            again= True
            resposta=False
        elif resposta == "n":
            again= False
            resposta=False
        else:
            print("valor invalido")
            resposta= True
    
    