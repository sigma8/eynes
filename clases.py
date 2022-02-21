from math import pi

class Circulo:

    def __init__(self, radius): 
        self.radius = radius
   
    def __mul__(self, other):
        self.radius = self.radius*other
        return f"El nuevo radio es: {self.radius}"
        
    def __str__(self) -> str:
        return f"Radio del circulo {self.radius}"

    def __repr__(self) -> str:
        return f"Circulo (radio={self.radius}"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius <= 0 :
            raise ValueError("El radio no puede ser menor o igual a cero")
        self._radius = radius
        if not isinstance(radius, (float, int)):
            raise TypeError("Radio debe ser un valor mayor a cero")
        self._radius = float(radius)
    
    def get_area(self):
        return f"El area del circulo es: {self.radius ** 2 * pi}"
    
    
    def get_perimetro(self):
        return f"El perimetro del circulo es: {self.radius * 2 * pi}"
    

if __name__ == '__main__':
    
    new_circulo = Circulo(4)

    print(new_circulo*2, new_circulo.get_area(), new_circulo.get_perimetro())


