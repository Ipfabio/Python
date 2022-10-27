Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def esBisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return f"El {anio} es bisiesto"
    else: return "No es bisiesto"


anio = input("Ingrese el año: ")

print(esBisiesto(int(anio)))

SyntaxError: invalid syntax
