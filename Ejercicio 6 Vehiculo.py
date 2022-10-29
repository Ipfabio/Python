class Vehiculo:
    color = "Azul"
    ruedas = 4
    puertas = 2

class Coche(Vehiculo):
    velocidad = 150
    cilindrada = 12

c = Coche()
print("El coche es",c)