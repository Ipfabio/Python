class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def apruebaONo(nota):
        if(nota > 6):
            print("Ha aprobado con {}",nota)
        else:
            print("Su nota es {}, no ha aprobado",nota)

alumn = Alumno("Marcos", 7)
print(alumn.apruebaONo)