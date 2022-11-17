# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
import sqlite3

conn = sqlite3.connect('ejercicio1.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE Alumnos(id INT, Nombre TEXT, Apellido TEXT)")

cursor.execute("INSERT INTO Alumnos VALUES(1,'Marcos', 'Marquitos')")
cursor.execute("INSERT INTO Alumnos VALUES(2,'Sofia', 'Sofi')")
cursor.execute("INSERT INTO Alumnos VALUES(3,'Lucas', 'Lu')")
cursor.execute("INSERT INTO Alumnos VALUES(4,'Lucia', 'Luli')")
cursor.execute("INSERT INTO Alumnos VALUES(5,'Daniela', 'Dani')")
cursor.execute("INSERT INTO Alumnos VALUES(6,'Micaela', 'Mica')")
cursor.execute("INSERT INTO Alumnos VALUES(7,'Diego', 'Diegote')")
cursor.execute("INSERT INTO Alumnos VALUES(8,'Esteban', 'Quito')")

conn.commit()

conn.execute("SELECT * FROM Alumnos WHERE Nombre = 'Esteban'")

rows = cursor.fetchall()

print(rows)

cursor.close()
conn.close()
