romanos= {
 'I': 1,
 'V': 5,
 'X': 10,
 'L': 50,
 'C': 100,
 'D': 500,
 'M': 1000,
}

def conversor( romano ):
    numero=0
    for algarismo in romano[::-1]:
        if romanos[algarismo]< numero:
            numero-=romanos[algarismo]
        else:
            numero+=romanos[algarismo]

    print(f"este numero é: {numero}")

conversor("mcd".upper())
