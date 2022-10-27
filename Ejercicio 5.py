Python 3.10.5
def esBisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return f"El {anio} es bisiesto"
    else: return "No es bisiesto"


anio = input("Ingrese el año: ")

print(esBisiesto(int(anio)))
