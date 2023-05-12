cpf=input('digite seu cpf (apenas numeros): ')
soma=0
multiplicador=10
for i in cpf:
    soma=soma +(int(i)*multiplicador)
    print(i,'*', multiplicador, soma)
    if multiplicador==2:
        break
    multiplicador-=1

digito_1= (soma*10)%11
if digito_1 >9:
    cpf[9]=='0'
elif digito_1<=9:
    cpf[9]== str(digito_1)
else:
    print('CPF invalido')

print('primeiro digito=', cpf[9])

soma=0
multiplicador=11
for i in cpf:
    soma=soma +(int(i)*multiplicador)
    print(i,'*', multiplicador, soma)
    if multiplicador==2:
        break
    multiplicador-=1

digito_2= (soma*10)%11
if digito_2 >9:
    cpf[10]=='0'
elif digito_2<=9:
    cpf[10]== str(digito_2)

print("segundo digito= ", digito_2)