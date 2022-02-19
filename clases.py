

class Circulo:
    def __init__(self, radio): 
        self.radio = radio

    def area(self):
        return self.radio**2*3.14

    def perimetro(self):
        return self.radio*2*3.14


circulo = Circulo(0)

print(circulo.area(), circulo.perimetro())
