from math import pi

from pip import main

class Circulo:


    def __init__(self, radius): 
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius <= 0 :
            raise ValueError("El radio no puede ser menor o igual a cero")
        self._radius = radius
        #if not isinstance(radius, (float, int)):
        #    raise TypeError("Radio debe ser un valor mayor a cero")
        #self._radius = float(radius)

    def get_area(self):
        return self.radius ** 2 * pi
    
    def get_perimetro(self):
        return self.radius * 2 * pi

if __name__ == '__main__':

    new_circulo = Circulo(2)

    print(new_circulo.get_area())
