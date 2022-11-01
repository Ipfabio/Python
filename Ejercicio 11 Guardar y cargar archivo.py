import pickle

class Vehiculo:
    marca = ""
    color = ""

    def __init__(self, modelo, color):
        self.marca = modelo
        self.color = color

    def __str__(self):
        return f'Este es un {self.marca} de color {self.color}'

coche = Vehiculo("Toyota", "azul")
print(coche)

f = open('vehiculo_obj', 'wb')

pickle.dump(coche, f)

f.seek(0)
nuevo_coche = pickle.load(f)

print(nuevo_coche)
f.close()