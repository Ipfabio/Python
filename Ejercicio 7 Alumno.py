class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def apruebaONo(self):
        if(self.nota > 6):
            print("Ha aprobado!")
        else:
            print("Su nota no es suficiente para aprobar")

alumno1 = Alumno()

alumno1.inicializar("Marcos", 7)

alumno1.imprimir()
alumno1.apruebaONo()