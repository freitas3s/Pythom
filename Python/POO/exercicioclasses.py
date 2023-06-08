
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_lados(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base*self.altura

    def perimetro(self):
        return self.base*2 + self.altura*2


retangulo1 = Retangulo(int(input("digite a base: ")),
                       int(input("digite a altura: "))
                       )

tamanho_piso = 10
tamanho_rodape = 1.25
pisos = 0
rodapes = 0
while retangulo1.area() > pisos*tamanho_piso:
    pisos += 1

while retangulo1.perimetro() > rodapes*tamanho_rodape:
    rodapes += 1

print(f"serão necessarios {pisos} pisos e {rodapes} rodapés")
