# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
f = open('archivo.txt', 'a')
f.write('Primera línea\n')
f.close()

f = open('archivo.txt','r+')
f.readline()
f.write('Segunda línea\n')

f.seek(0)
print(f.read())
f.close
