import math

class Triangle:
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular(self):
        area = (self.lado1*self.lado2/2) 

        h = pow(self.lado1,2) + pow(self.lado2,2)
        hipotenusa = math.trunc(math.sqrt(h))
        
        perimetro = (self.lado1 + self.lado2 + hipotenusa)

        angulo1 = math.trunc(math.degrees(math.atan(self.lado1 / hipotenusa)))
        angulo2 = math.trunc(math.degrees(math.atan(self.lado2 / hipotenusa)))

        print(f'Área: {area}\nPerimetro: {perimetro}\nHipotenusa: {hipotenusa}\nÁngulo 1: {angulo1}\nÁngulo 2: {angulo2}')

mi_triangulo = Triangle(5,10) 
mi_triangulo.calcular()