nota1=int(input("digite a nota do teste: "))
nota2=int(input("digite a nota da prova: "))
media=(nota1+nota2)/2

if media>60:
    print(media)
    print("aprovado")
else:
    print(media)
    print("reprovado")