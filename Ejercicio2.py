from functools import reduce

# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter
# y realizará una suma de todos estos elementos obtenidos mediante reduce.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def mifuncion(x):
    if x % 2 != 0:
        return True
    else:
        return False


resultado = list(filter(mifuncion, lista))
# resultado =list(filter(lambda numero: numero % 2 != 0, lista)) Version Lambda

print("numero impares:", resultado)
print("Sumados:", reduce(lambda x, y: x + y, resultado))

# version con función
# def suma(a,b):
#     for numero in resultado:
#         return a + b
#
# print(reduce(suma,resultado))
